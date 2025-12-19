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

ALL_CANDIDATES = { # ID -> {name, img_half, img_avatar} 全量干员库
    "op01": {"name": "烛煌", "img_half": "https://free.picui.cn/free/2025/12/18/6943b4349298e.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45f8673b.png"},
    "op02": {"name": "余", "img_half": "https://free.picui.cn/free/2025/12/18/6943b433c5939.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45d1a96f.png"},
    "op03": {"name": "隐德来希", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42f4d334.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45b81b00.png"},
    "op04": {"name": "死芒", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42a1ac92.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4579ec8d.png"},
    "op05": {"name": "Mon3tr", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42566f19.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4521f702.png"},
    "op06": {"name": "信仰搅拌机", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42ec4bda.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45ae41f7.png"},
    "op07": {"name": "蕾缪安", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425c47fb.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45201995.png"},
    "op08": {"name": "新约能天使", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42e928d0.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45ab16dd.png"},
    "op09": {"name": "酒神", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425c5a82.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4523adbe.png"},
    "op10": {"name": "司霆惊蛰", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42a0c471.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4576fea9.png"},
    "op11": {"name": "电弧", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425974ac.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b451cd283.png"},
    "op12": {"name": "遥", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42edce4c.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45b6aa4e.png"},
    "op13": {"name": "斩业星熊", "img_half": "https://free.picui.cn/free/2025/12/18/6943b4341b82d.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45e9995e.png"},
    "op14": {"name": "丰川祥子", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425c1274.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45253f65.png"},
    "op15": {"name": "真言", "img_half": "https://free.picui.cn/free/2025/12/18/6943b43447640.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45f5f50e.png"},
    "op16": {"name": "溯光星源", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42e3a657.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45997abc.png"},
    "op17": {"name": "圣聆初雪", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429da319.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4575e451.png"},
    "op18": {"name": "凛御银灰", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429670fd.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b455e1218.png"},
    "op19": {"name": "娜斯提", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429e020b.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b456ce71d.png"}
}

# 奖项配置结构
# 结构：ID -> {标题, 副标题, 候选人列表, 允许选几个, 分数权重}
VOTE_CATEGORIES = [
    # TODO:
    # Speical:昨夜圆车
    {
        "id": "best_support",
        "title": "最佳援助",
        "subtitle": "即使是看似最微小的工作，干员们也会全力以赴。何况事实上，一点也不微小。",
        "max_choices": 3,
        "weights": [5, 3, 2],
        "candidates_ids": [
            "op02", "op05", "op08", "op09", "op11",
            "op12", "op16", "op18", "op19"
        ]
    },
    {
        "id": "best_damage",
        "title": "最佳输出",
        "subtitle": "手段有很多，结局却只有一种。",
        "max_choices": 3,
        "weights": [5, 3, 2],
        "candidates_ids": [
            "op01", "op03", "op04", "op05", "op07",
            "op08", "op10", "op13", "op14", "op15",
            "op17"
        ]
    },
    {
        "id": "best_controversial",
        "title": "最具争议",
        "subtitle": "\"谁来审判？\"",
        "max_choices": 2,
        "weights": [5, 4],
        "candidates_ids": [
            "op02", "op03", "op04", "op11", "op13",
            "op14", "op15", "op18"
        ]
    },
    {
        "id": "best_vanilla",
        "title": "最香草（",
        "subtitle": "终于欲望吧...",
        "max_choices": 3,
        "weights": [5, 3, 2],
        "candidates_ids": [
            "op01", "op02", "op03", "op04", "op05",
            "op06", "op07", "op08", "op09", "op10",
            "op11", "op12", "op13", "op14", "op15",
            "op16", "op17", "op18", "op19"
        ]
    },
    {
        "id": "best_story",
        "title": "最佳剧情塑造",
        "subtitle": "有些故事，注定无法被遗忘。",
        "max_choices": 3,
        "weights": [5, 3, 2],
        "candidates_ids": [
            "op01", "op02", "op03", "op04", "op05",
            "op06", "op07", "op08", "op09", "op10",
            "op11", "op12", "op13", "op14", "op15",
            "op16", "op17", "op18", "op19"
        ]
    },
    {
        "id": "best_inflation",
        "title": "最强度通胀",
        "subtitle": "你知道吗，到2025年末，超大杯干员已经有41名。",
        "max_choices": 3,
        "weights": [5, 3, 2],
        "candidates_ids": [
            "op05", "op08", "op09", "op12", "op14",
            "op17"
        ]
    },
    {
        "id": "best_constriction",
        "title": "最强度紧缩",
        "subtitle": "正稳步推进\"一百个百嘉计划\"。",
        "max_choices": 2,
        "weights": [5, 4],
        "candidates_ids": [
            "op03", "op04", "op16", "op19"
        ]
    },
    {
        "id": "six_star_2025",
        "title": "2025年度六星干员",
        "subtitle": "欢迎来到，罗德岛——",
        "max_choices": 4,
        "weights": [10, 7, 5, 4],
        "candidates_ids": [
            "op01", "op02", "op03", "op04", "op05",
            "op06", "op07", "op08", "op09", "op10",
            "op11", "op12", "op13", "op14", "op15",
            "op16", "op17", "op18", "op19"
        ]
    }
]

# 校验辅助函数：确保每个奖项的 weights 长度 >= max_choices
for cat in VOTE_CATEGORIES:
    assert len(cat['weights']) >= cat['max_choices'], f"配置错误: {cat['title']} 的权重数量少于允许选择的数量"