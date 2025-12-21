# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config, VOTE_CATEGORIES, ALL_CANDIDATES
from config import BOSS_POOL, SP_CATEGORY
from models import db, VoteRecord
from datetime import datetime

VOTE_DEADLINE = datetime(2026, 1, 1, 0, 0, 0)

app = Flask(__name__)
app.config.from_object(Config)
CORS(app) # 允许前端跨域访问
db.init_app(app)

# 初始化数据库（第一次运行时创建文件）
with app.app_context():
    db.create_all()

def is_vote_ended():
    return datetime.now() >= VOTE_DEADLINE

# ---------------------------------------------------------
# API 1: 获取配置 (前端根据这个动态生成页面)
# ---------------------------------------------------------
@app.route('/api/config', methods=['GET'])
def get_config():

    if is_vote_ended():
        return jsonify({"error": "投票已截止，感谢参与！"}), 403

    # 动态拼装完整配置
    full_categories = []
    
    for cat in VOTE_CATEGORIES:

        if not cat.get('is_sp'):
            # 将 ID 列表转换为 包含详情的对象列表
            detailed_candidates = []
            for cand_id in cat['candidates_ids']:
                cand_info = ALL_CANDIDATES.get(cand_id, {})
                detailed_candidates.append({
                    "id": cand_id,
                    **cand_info # 将 name, img_half, img_avatar 解构进去
                })
            
            # 构建返回给前端的奖项对象
            full_categories.append({
                "id": cat['id'],
                "title": cat['title'],
                "subtitle": cat['subtitle'],
                "max_choices": cat['max_choices'],
                "candidates": detailed_candidates # 拼装好的完整数据
            })
            
        # --- SP 奖项逻辑 (Boss DLC) ---
        else:
            detailed_themes = []
            for theme in cat['themes']:
                detailed_boxes = []
                for box in theme['boxes']:
                    # 加入 if cid in ALL_CANDIDATES 判断
                    boss_details = [{**ALL_CANDIDATES[cid], "id": cid} for cid in box['cands'] if cid in ALL_CANDIDATES]
                    detailed_boxes.append({
                        "id": box['id'],
                        "boss_details": boss_details
                    })
                detailed_themes.append({"title": theme['title'], "boxes": detailed_boxes})
            
            full_categories.append({
                "id": cat['id'], "is_sp": True, "title": cat['title'], 
                "subtitle": cat['subtitle'], "max_choices": cat['max_choices'],
                "themes": detailed_themes
            })
            
    return jsonify({"categories": full_categories})

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
    # existing_vote = VoteRecord.query.filter_by(ip_address=user_ip, category_id=cat_id).first()
    # if existing_vote:
    #     return jsonify({"status": "error", "message": "您已经投过该奖项了"}), 403

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

    # 遍历配置中的每一个奖项
    for cat in VOTE_CATEGORIES:
        cat_id = cat['id']
        weights = cat.get('weights', [1])  # 获取权重，默认至少为1分
        
        # 初始化该奖项下每个干员的分数为0
        scores = {cand_id: 0 for cand_id in cat['candidates_ids']}

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

@app.route('/api/sp/config', methods=['GET'])
def get_sp_config():
    """获取 Boss DLC 专用的详细配置"""
    detailed_themes = []
    for theme in SP_CATEGORY['themes']:
        detailed_boxes = []
        for box in theme['boxes']:
            # 从独立的 BOSS_POOL 中提取数据
            boss_list = [{**BOSS_POOL[bid], "id": bid} for bid in box['cands']]
            detailed_boxes.append({
                "id": box['id'],
                "boss_details": boss_list
            })
        detailed_themes.append({"title": theme['title'], "boxes": detailed_boxes})
    
    return jsonify({
        "title": SP_CATEGORY['title'],
        "subtitle": SP_CATEGORY['subtitle'],
        "max_choices": SP_CATEGORY['max_choices'],
        "themes": detailed_themes
    })

@app.route('/api/sp/submit', methods=['POST'])
def submit_sp_vote():
    """提交 Boss 投票"""

    if is_vote_ended():
        return jsonify({"error": "投票已截止，感谢参与！"}), 403

    data = request.json
    box_ids = data.get('box_ids', [])
    if len(box_ids) > SP_CATEGORY['max_choices']:
        return jsonify({"error": "超出最大选择数"}), 400
    
    new_vote = VoteRecord(
        ip_address=request.remote_addr,
        category_id=SP_CATEGORY['id'],
        choices=",".join(box_ids)
    )
    db.session.add(new_vote)
    db.session.commit()
    
    return jsonify({"message": "记忆已成功同步"})

@app.route('/api/sp/stats', methods=['GET'])
def get_sp_stats():
    """获取 Boss 投票统计结果（带详细信息）"""

    records = VoteRecord.query.filter_by(category_id=SP_CATEGORY['id']).all()
    stats_map = {}
    weights = SP_CATEGORY.get('weights')
    
    for rec in records:
        selected_boxes = rec.choices.split(',')
        for idx, b_id in enumerate(selected_boxes):
            weight = weights[idx] if idx < len(weights) else 1
            stats_map[b_id] = stats_map.get(b_id, 0) + weight

    results = []
    for box_id, score in stats_map.items():
        box_detail = None

        for theme in SP_CATEGORY['themes']:
            for box in theme['boxes']:
                if box['id'] == box_id:
                    boss_list = [{**BOSS_POOL[bid], "id": bid} for bid in box['cands']]
                    box_detail = {
                        "id": box_id,
                        "score": score,
                        "theme_title": theme['title'],
                        "bosses": boss_list
                    }
                    break
            if box_detail: break
        
        if box_detail:
            results.append(box_detail)

    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)[:10]
    return jsonify({"stats": sorted_results})

if __name__ == '__main__':
    app.run(debug=True, port=5000)