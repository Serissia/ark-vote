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
    # TODO：最佳输出副标题：手段有很多，结局却只有一种。
    # 最佳节奏（“谁来审判？”）；最佳剧情；
    # 最佳强度通胀（你知道吗，到2025年末，超大杯干员已经有41名）；
    # 最佳强度紧缩（正稳步推进“一百个百嘉计划”）
    {
        "id": "best_support",
        "title": "最佳援助干员",
        "subtitle": "即使是看似最微小的工作，干员们也会全力以赴。何况事实上，一点也不微小。",
        "max_choices": 3,  # 最多选3个
        "weights": [5, 3, 2], # 对应 mark[i][j] 分值
        "candidates": [
            {"id": "mon3tr", "name": "Mon3tr", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42566f19.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4521f702.png"},
            {"id": "jiushen", "name": "酒神", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425c5a82.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4523adbe.png"},
            {"id": "dianhu", "name": "电弧", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425974ac.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b451cd283.png"},
            {"id": "yao", "name": "遥", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42edce4c.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45b6aa4e.png"},
            {"id": "suguangxingyuan", "name": "溯光星源", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42e3a657.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45997abc.png"},
            {"id": "linyuyinhui", "name": "凛御银灰", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429670fd.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b455e1218.png"},
            {"id": "nasiti", "name": "娜斯提", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429e020b.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b456ce71d.png"}
        ]
    },
    {
        "id": "six_star_2025",
        "title": "2025年度六星干员",
        "subtitle": "别问我为什么没抽到，问就是为了在这个列表里看他们一眼。", #
        "max_choices": 4,  # 最多选4个
        "weights": [10, 7, 5, 3], # 对应 mark[i][j] 分值
        "candidates": [
            {"id": "zhuhuang", "name": "烛煌", "img_half": "https://free.picui.cn/free/2025/12/18/6943b4349298e.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45f8673b.png"},
            {"id": "yu", "name": "余", "img_half": "https://free.picui.cn/free/2025/12/18/6943b433c5939.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45d1a96f.png"},
            {"id": "yindelaixi", "name": "隐德来希", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42f4d334.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45b81b00.png"},
            {"id": "simang", "name": "死芒", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42a1ac92.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4579ec8d.png"},
            {"id": "mon3tr", "name": "Mon3tr", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42566f19.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4521f702.png"},
            {"id": "jiaobanji", "name": "信仰搅拌机", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42ec4bda.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45ae41f7.png"},
            {"id": "leimiuan", "name": "蕾缪安", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425c47fb.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45201995.png"},
            {"id": "nengtianshi_alt", "name": "新约能天使", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42e928d0.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45ab16dd.png"},
            {"id": "jiushen", "name": "酒神", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425c5a82.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4523adbe.png"},
            {"id": "sitingjingzhe", "name": "司霆惊蛰", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42a0c471.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4576fea9.png"},
            {"id": "dianhu", "name": "电弧", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425974ac.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b451cd283.png"},
            {"id": "yao", "name": "遥", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42edce4c.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45b6aa4e.png"},
            {"id": "zhanyexingxiong", "name": "斩业星熊", "img_half": "https://free.picui.cn/free/2025/12/18/6943b4341b82d.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45e9995e.png"},
            {"id": "xiangzi", "name": "丰川祥子", "img_half": "https://free.picui.cn/free/2025/12/18/6943b425c1274.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45253f65.png"},
            {"id": "zhenyan", "name": "真言", "img_half": "https://free.picui.cn/free/2025/12/18/6943b43447640.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45f5f50e.png"},
            {"id": "suguangxingyuan", "name": "溯光星源", "img_half": "https://free.picui.cn/free/2025/12/18/6943b42e3a657.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b45997abc.png"},
            {"id": "shenglingchuxue", "name": "圣聆初雪", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429da319.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b4575e451.png"},
            {"id": "linyuyinhui", "name": "凛御银灰", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429670fd.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b455e1218.png"},
            {"id": "nasiti", "name": "娜斯提", "img_half": "https://free.picui.cn/free/2025/12/18/6943b429e020b.png", "img_avatar": "https://free.picui.cn/free/2025/12/18/6943b456ce71d.png"}
        ]
    }
]

# 校验辅助函数：确保每个奖项的 weights 长度 >= max_choices
for cat in VOTE_CATEGORIES:
    assert len(cat['weights']) >= cat['max_choices'], f"配置错误: {cat['title']} 的权重数量少于允许选择的数量"