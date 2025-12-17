# backend/config.py

class Config:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///votes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# ==========================================
# 投票核心配置
# ==========================================

# 全局限制常量
MAX_VOTES_PER_IP = 1  # 简单防刷：每个IP限制投几次

# 奖项配置结构
# 结构：ID -> {标题, 副标题, 候选人列表, 允许选几个, 分数权重}
VOTE_CATEGORIES = [
    {
        "id": "best_medic",
        "title": "最佳治疗干员",
        "subtitle": "把敌人全解决掉是最好的治疗……什么，你当真了？",
        "max_choices": 3,  # 该奖项最多选3人
        # 对应 mark[i][j]: 第1名得10分，第2名7分，第3名5分
        "weights": [10, 7, 5], 
        "candidates": [
            {"id": "kaltsit", "name": "凯尔希", "img_half": "url_to_half_kaltsit", "img_avatar": "url_to_head_kaltsit"},
            {"id": "eyja_alt", "name": "纯烬艾雅法拉", "img_half": "url_to_half_eyja", "img_avatar": "url_to_head_eyja"},
            {"id": "reed_alt", "name": "焰影苇草", "img_half": "url_to_half_reed", "img_avatar": "url_to_head_reed"},
            # ... 更多干员
        ]
    },
    {
        "id": "best_vanguard",
        "title": "最佳先锋干员",
        "subtitle": "谁说先锋就只能回费？",
        "max_choices": 2,
        "weights": [10, 5], # 只选2人，第一名10分，第二名5分
        "candidates": [
            {"id": "ines", "name": "伊内丝", "img_half": "...", "img_avatar": "..."},
            {"id": "muelsyse", "name": "缪尔赛思", "img_half": "...", "img_avatar": "..."},
        ]
    }
]

# 校验辅助函数：确保每个奖项的 weights 长度 >= max_choices
for cat in VOTE_CATEGORIES:
    assert len(cat['weights']) >= cat['max_choices'], f"配置错误: {cat['title']} 的权重数量少于允许选择的数量"