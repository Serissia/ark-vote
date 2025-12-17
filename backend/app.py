# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config, VOTE_CATEGORIES
from models import db, VoteRecord

app = Flask(__name__)
app.config.from_object(Config)
CORS(app) # 允许前端跨域访问
db.init_app(app)

# 初始化数据库（第一次运行时创建文件）
with app.app_context():
    db.create_all()

# ---------------------------------------------------------
# API 1: 获取配置 (前端根据这个动态生成页面)
# ---------------------------------------------------------
@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify({
        "status": "success",
        "categories": VOTE_CATEGORIES
    })

# ---------------------------------------------------------
# API 2: 提交投票
# ---------------------------------------------------------
@app.route('/api/vote', methods=['POST'])
def submit_vote():
    data = request.json
    # 预期数据格式: 
    # { 
    #   "category_id": "best_medic", 
    #   "choices": ["kaltsit", "reed_alt"]  (按顺序排列，第一个是第一名)
    # }
    
    user_ip = request.remote_addr
    cat_id = data.get('category_id')
    user_choices = data.get('choices', [])

    # 1. 查找对应的奖项配置
    category_config = next((item for item in VOTE_CATEGORIES if item["id"] == cat_id), None)
    if not category_config:
        return jsonify({"status": "error", "message": "无效的奖项ID"}), 400

    # 2. 验证：选择数量是否超标？
    if len(user_choices) > category_config['max_choices']:
        return jsonify({"status": "error", "message": "选择的干员数量过多"}), 400
    
    # 3. 验证：是否重复投票？
    existing_vote = VoteRecord.query.filter_by(ip_address=user_ip, category_id=cat_id).first()
    if existing_vote:
        return jsonify({"status": "error", "message": "您已经投过该奖项了"}), 403

    # 4. 保存入库
    new_vote = VoteRecord(
        ip_address=user_ip,
        category_id=cat_id,
        choices=",".join(user_choices) # 存为 "kaltsit,reed_alt"
    )
    db.session.add(new_vote)
    db.session.commit()

    return jsonify({"status": "success", "message": "投票记录已保存"})

# ---------------------------------------------------------
# API 3: 获取统计数据 (含加权计算逻辑)
# ---------------------------------------------------------
@app.route('/api/stats', methods=['GET'])
def get_stats():
    stats_result = {}

    for cat in VOTE_CATEGORIES:
        cat_id = cat['id']
        weights = cat['weights']
        
        # 初始化该奖项下每个干员的分数为0
        scores = {candidate['id']: 0 for candidate in cat['candidates']}
        
        # 从数据库捞出该奖项的所有投票
        votes = VoteRecord.query.filter_by(category_id=cat_id).all()
        
        for vote in votes:
            choices_list = vote.choices.split(',')
            # 核心算法：遍历用户的选择，根据次序赋予权重
            # enumerate(choices_list) 会返回 (0, "kaltsit"), (1, "reed_alt")...
            for index, candidate_id in enumerate(choices_list):
                if index < len(weights) and candidate_id in scores:
                    # 分数 += 对应排名的权重
                    scores[candidate_id] += weights[index]
        
        # 整理输出格式，按分数从高到低排序
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        stats_result[cat_id] = sorted_scores

    return jsonify({
        "status": "success",
        "stats": stats_result
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)