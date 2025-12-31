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

BOSS_POOL = {
    "boss01": {
        "name": "无餍", 
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945523b3b294.png",
        "desc": "自如梦方醒的岁的代理人心中诞生的化物，大口吞噬着失意之情。相聚是滋味，思念何尝不是？欢愉是滋味，悲切何尝不是？得意是滋味，悔恨何尝不是？"
    },
    "boss02": {
        "name": "“万火归一”", 
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455247785ff.png",
        "desc": "盘踞于原野之上，永不离去的红龙先祖，抑或只是众心所向的还火之地。新火不断被抛掷于旧火之上，一切终结，同时一切诞生。"
    },
    "boss03": {
        "name": "PRTS，“源代码”", 
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455249875d2.png",
        "desc": "PRTS的原始代码覆写了权限，它开始抹除你们在罗德岛上留存的一切痕迹。"
    },
    "boss04": {
        "name": "拟态机械", 
        "img_avatar": "https://free.picui.cn/free/2025/12/20/69462f7bec9e1.png", "desc": "PRTS将存储数据中罗德岛的熟悉之物变成了实体的威胁，绝对理性的机械不会理解何为恐惧。",
        "desc": "PRTS将存储数据中罗德岛的熟悉之物变成了实体的威胁，绝对理性的机械不会理解何为恐惧。"
    },
    "boss05": {
        "name": "“圣徒”", 
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455246a9169.png", 
        "desc": "拉特兰最初的圣徒。曾经，还是提卡兹的它与“律法”相遇，“萨科塔”自此始，拉特兰自此始。"
    },
    "boss06": {
        "name": "“Mechanist”，机械之心", 
        "img_avatar": "https://free.picui.cn/free/2025/06/29/6860f03f62555.png", 
        "desc": "以Mechanist的战力极限为模本构拟的突破训练官。以严谨和记忆力著称的工程师，但也曾在某次酒后写下“爱就像热力学第二定律，越是渴望永恒，越是走向衰退。”这样的诗句。"
    },
    "boss07": {
        "name": "结构性原理", 
        "img_avatar": "https://free.picui.cn/free/2025/06/29/6860f03f600fb.png", 
        "desc": "Mechanist亲手制造的风险排查机械，是他最好的朋友。为了不让可露希尔染指这台机械，他设置了二十道防御程序。"
    },
    "boss08": {
        "name": "“酒神”", 
        "img_avatar": "https://free.picui.cn/free/2025/12/19/694552439ff9e.png", 
        "desc": "死亡常在，戏剧永恒。"
    },
    "boss09": {
        "name": "坎某人",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945525195b9c.png",
        "desc": "行走于园林的神秘商人兼鲍老板下属，只要典籍里存在的，他就贩卖。"
    },
    "boss10": {
        "name": "夕娥",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945523b6cecf.png",
        "desc": "大炎民间所传颂的，奔赴双月寻夫的奇女子。古代传说有不少超越了今日人力所能及的范围，戏说与记事的分界有时也变得极为模糊。"
    },
    "boss11": {
        "name": "双月共主",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455236c4320.png",
        "desc": "因着奔月的传说，夕娥在民间成了双月的象征。但如果，奔上月亮也寻不到夫君踪迹，或许，她会一跃而上，步入几无尽头的虚空吧。"
    },
    "boss12": {
        "name": "玉双剑",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945523ee2703.png",
        "desc": "擅使剑的侠客，活跃于百氏之乱期间，以仁德闻名天下。话虽如此，他的宽厚也拂不尽人心黑暗。"
    },
    "boss13": {
        "name": "枣大刀",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945523a00073.png",
        "desc": "擅使刀的侠客，活跃于百氏之乱期间，以忠义闻名天下。话虽如此，他的赤诚也没能胜过乱世烟云。"
    },
    "boss14": {
        "name": "炭长矛",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455236d8a95.png",
        "desc": "擅使矛的侠客，活跃于百氏之乱期间，以武勇闻名天下。话虽如此，他的力量也没能扫尽邪佞。"
    },
    "boss15": {
        "name": "昭烈君",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455240315e2.png",
        "desc": "被供奉于侠君祠的人物，三侠客之首，纵是身死，也要扬善除恶，留得清白在人间。数方势力因其而殒，正统得以归炎。"
    },
    "boss16": {
        "name": "文衡君",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945523a00073.png",
        "desc": "被供奉于侠君祠的人物，三侠客中排名第二，纵是身死，也要破关斩将，夺回大哥尸首，归田安葬。"
    },
    "boss17": {
        "name": "桓君",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455236d8a95.png",
        "desc": "被供奉于侠君祠的人物，三侠客中排名第三，纵是身死，也要横立桥廊，怒目圆睁，敌酋军将虽多，无人可过其侧。"
    },
    "boss18": {
        "name": "师祖",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455236e4601.png",
        "desc": "天师之祖，有动天覆地的本领，然而辅佐炎氏正位后便再无踪迹，传说有人见过他骑着瑞兽在江边垂钓的身影。"
    },
    "boss19": {
        "name": "太公",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455236d7b0e.png",
        "desc": "太公姓姜，取其姓氏命名的地域名为姜齐，他虽被大炎册封，但从未就任。庙堂之上未曾见其身影。唯山水相逢，人力不及处，或可有缘一见。这可能就是天师府喜欢修建在崇山峻岭间的原因。"
    },
    "boss20": {
        "name": "易",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945523cc430c.png",
        "desc": "揉梁染柱，聚楼生阁，采云泥以为物，取相合以成对。"
    },
    "boss21": {
        "name": "“岁”",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/694552474fd1f.png",
        "desc": "大炎最后射落的神明半梦半醒间显现的样貌。一位代理人替换了其中的意义，以身代岁，似要令其完全苏醒。"
    },
    "boss22": {
        "name": "“望”",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455247b5ae7.png",
        "desc": "谋臣、罪人，于岁陵置下的一手。"
    },
    "boss23": {
        "name": "后兽",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524c69378.png",
        "desc": "与地同形，与山同齐，万类难及，以后名之。"
    },
    "boss24": {
        "name": "矩兽",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455250a37ef.png",
        "desc": "溯合制序，止攻泯灾，刚而难曲，以矩名之。"
    },
    "boss25": {
        "name": "三船光平",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455255aa354.png",
        "desc": "他的刀不谈任侠，不论英雄，只替浪潮肃清去路——哪怕在路途尽头，他自己也将成为无名泡沫。"
    },
    "boss26": {
        "name": "莫菲丝",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455253d4ae4.png",
        "desc": "梦中的一切明明这么有趣，为什么还想要逃离呢......留在这里多好。"
    },
    "boss27": {
        "name": "“徘徊者”",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455245636f2.png",
        "desc": "无论血缘相近，还是遭遇相同，他与他的兄弟最终都踏上了同样一条路，成为了荒野怪谈的一部分，成为了斥绝生命，拥抱源石的存在。"
    },
    "boss28": {
        "name": "恩慈祷者",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524b17d72.png",
        "desc": "她的虔诚与仁爱有口皆碑，无数人因其施以援手而得以幸存。然而心灵的坚韧敌不过生理的转变，当她从棺椁中醒来时，她所拯救的，也将由她吃食。"
    },
    "boss29": {
        "name": "斑斓虫",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524a673a5.png",
        "desc": "颚虫种群中稀少的王虫，巨锹虫是她的卫士，小颚虫是她的子民，接受到其信息素的颚虫会不顾一切地执行指令。通常一个种群中只会有一只王虫，若有新王虫出现，老王虫会自我退化。而其被称作斑斓虫的原因，在激怒她后便可知晓。"
    },
    "boss30": {
        "name": "“老尖牙”",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455244f41d7.png",
        "desc": "生物与人一样会遭受感染，当生命步入末期时，再高傲的猎手也终将躺倒在地，化作尘齑。然而，在罗德岛沉没，造物主苏醒的时刻之后，有一些亘古不变的常理，也悄然发生了变化。"
    },
    "boss31": {
        "name": "狂躁异质裂兽",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455252526bf.png",
        "desc": "它早已失去神识，唯一支撑它的，只有求生的本能。"
    },
    "boss32": {
        "name": "圣愚",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455236972b1.png",
        "desc": "不断忍耐，不做选择，不必挣扎......最后，接受它。"
    },
    "boss33": {
        "name": "披挂冰雪的少女",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/69455254b3015.png",
        "desc": "披挂着冰霜与漫长往昔的少女，她只是长久地沉默，你在其平静的表情之下看到复杂的悲悯、遗憾、释然与决心。"
    },
    "boss34": {
        "name": "耶拉冈德",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945523c66641.png",
        "desc": "如白雪一般无边际而美丽的巨大生物。祂摄人心魄，恢弘而伟大，远超你所见、所曾见、所能见的一切。"
    },
    "boss35": {
        "name": "假想敌：胄",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524fbf25a.png",
        "desc": "被源石完全侵蚀的蒸汽甲胄，是根据源石灾难在全泰拉爆发的想象而设计的假想敌之一。源石在大地上蔓延，曾经的勇气、信念与荣耀皆归于晶尘，只留被晶簇撕裂的甲胄仍向那余晖落幕之地前行。"
    },
    "boss36": {
        "name": "假想敌：管",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524f476d4.png",
        "desc": "由源石创造再现的“女皇之声”，是根据源石灾难在全泰拉爆发的想象而设计的假想敌之一。源石在大地上蔓延，淹没一切赞美与斥责。晶体棱面泛起的余音，不过是源石的另一个名字。"
    },
    "boss37": {
        "name": "假想敌：铳",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524dcafa8.png",
        "desc": "被源石占据重塑的圣卫铳骑，是根据源石灾难在全泰拉爆发的想象而设计的假想敌之一。源石在大地上蔓延，夺去一切我们尊崇的事物并取而代之，当所有的秩序被粉碎，它即是秩序。"
    },
    "boss38": {
        "name": "女妖河谷的拂哀菈",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945525462e66.png",
        "desc": "只要能再做些什么，为河谷，为女妖，为那个孩子。"
    },
    "boss39": {
        "name": "“晨音”",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/694552433cbc2.png",
        "desc": "化为器伥的编钟。其主人生前是一名乐师，去世前委托杜小姐将编钟送给自己的朋友。被盗走后，偶然受到岁相影响化作器伥。不知主人已死，想要回到主人身边而四处徘徊，摇摇晃晃发出的声响令人神伤。"
    },
    "boss40": {
        "name": "“绝对安保”试做型",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524456504.png",
        "desc": "多索雷斯某家初创公司为克里斯达尔艺术馆量身定做的安保机器人，他们欠下许多外债，指望靠这笔生意一炮而红。雷内尔曾承诺会在收货后三天内付清货款，可直到那家公司被催债人用推土机夷为平地，雷内尔都没掏出一分钱，他甚至没有拆封这台耗费大量心血的机器——也许他只是想看着那群聪明人被逼疯，谁知道呢？"
    },
    "boss41": {
        "name": "冰滚兽",
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524ae4f1e.png",
        "desc": "已经看不出本来模样的巨型野兽。似乎是某种穴居动物，对挖掘巢穴有着巨大的热情，视力很差，全身覆有坚冰鳞片，行动时会将自身缩成一团，以翻滚的方式移动。"
    },
    "boss42": {
        "name": "“阿米娅”，炉芯终曲", 
        "img_avatar": "https://free.picui.cn/free/2025/12/19/6945524047733.png", 
        "desc": "存在于每个故事尽头，带走每位角色，封闭每种可能，停止每段讲述。它是对终结的想象，亦是所有想象的终结，它是一切，唯独不是你熟悉的人。"
    }
}

# ALL_CANDIDATES.update(BOSS_POOL)

# 奖项配置结构
# 结构：ID -> {标题, 副标题, 候选人列表, 允许选几个, 分数权重}
VOTE_CATEGORIES = [
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
        "subtitle": "忠于欲望吧...",
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

SP_CATEGORY = {
    "id": "six_star_alter_2025",
    "is_sp": True,
    "title": "2025年度干员",
    "subtitle": "我...我全都想起来了...我是...整合运动的大学生...",
    "max_choices": 7,
    "weights": [10, 9, 8, 7, 6, 5, 4],
    "themes": [
        {"title": "相见欢", "boxes": [{"id": "box01", "cands": ["boss01"]}]},
        {"title": "挽歌燃烧殆尽", "boxes": [{"id": "box02", "cands": ["boss02"]}]},
        {"title": "EP15 离解复合", "boxes": [{"id": "box03", "cands": ["boss03", "boss04"]}]}, # 共享 CandBox
        {"title": "众生行记", "boxes": [{"id": "box04", "cands": ["boss05"]}]},
        {"title": "矢量突破#1 「无机物」", "boxes": [{"id": "box05", "cands": ["boss06", "boss07"]}]},
        {"title": "红丝绒", "boxes": [{"id": "box06", "cands": ["boss08"]}]},
        {"title": "集成战略#6 「岁的界园志异」", "boxes": [
            {"id": "box07", "cands": ["boss09"]},
            {"id": "box08", "cands": ["boss10", "boss11"]},
            {"id": "box09", "cands": ["boss12", "boss13", "boss14", "boss15", "boss16", "boss17"]},
            {"id": "box10", "cands": ["boss18", "boss19"]},
            {"id": "box11", "cands": ["boss20"]},
            {"id": "box12", "cands": ["boss21"]},
            {"id": "box13", "cands": ["boss22"]},
            {"id": "box14", "cands": ["boss23", "boss24"]},
        ]},
        {"title": "墟", "boxes": [{"id": "box15", "cands": ["boss25"]}]},
        {"title": "无忧梦呓", "boxes": [{"id": "box16", "cands": ["boss26"]}]},
        {"title": "次生预案", "boxes":[
            {"id": "box17", "cands": ["boss27"]},
            {"id": "box18", "cands": ["boss28"]},
            {"id": "box19", "cands": ["boss29"]},
            {"id": "box20", "cands": ["boss30"]}
        ]},
        {"title": "EP16 反常光谱", "boxes": [
            {"id": "box21", "cands": ["boss31"]},
            {"id": "box22", "cands": ["boss32"]}
        ]},
        {"title": "雪山降临1101", "boxes": [
            {"id": "box23", "cands": ["boss33", "boss34"]}
        ]},
        {"title": "卫戍协议：盟约", "boxes": [
            {"id": "box24", "cands": ["boss35"]},
            {"id": "box25", "cands": ["boss36"]},
            {"id": "box26", "cands": ["boss37"]}
        ]},
        {"title": "未许之地", "boxes": [{"id": "box27", "cands": ["boss38"]}]},
        {"title": "保全派驻", "boxes": [
            {"id": "box28", "cands": ["boss39"]},
            {"id": "box29", "cands": ["boss40"]},
            {"id": "box30", "cands": ["boss41"]}
        ]},
        {"title": "集成战略#5 「萨卡兹的无终奇语」 内容拓展Ⅱ：无瑕之日", "boxes": [
            {"id": "box31", "cands": ["boss42"]}
        ]}
    ]
}

# VOTE_CATEGORIES.append(SP_CATEGORY)

# 校验辅助函数：确保每个奖项的 weights 长度 >= max_choices
for cat in VOTE_CATEGORIES:
    assert len(cat['weights']) >= cat['max_choices'], f"配置错误: {cat['title']} 的权重数量少于允许选择的数量"