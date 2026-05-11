"""
食物数据库 - 包含常见食物的营养信息
每 100g 可食部分的数据
"""

FOOD_DATABASE = {
    # 主食类
    "米饭": {"calories": 116, "protein": 2.6, "fat": 0.3, "carbs": 25.9},
    "馒头": {"calories": 223, "protein": 7.0, "fat": 1.1, "carbs": 47.0},
    "面条": {"calories": 110, "protein": 2.7, "fat": 0.7, "carbs": 24.3},
    "面包": {"calories": 265, "protein": 8.0, "fat": 3.5, "carbs": 50.6},
    "燕麦": {"calories": 376, "protein": 13.0, "fat": 6.7, "carbs": 67.0},
    "玉米": {"calories": 112, "protein": 4.0, "fat": 1.2, "carbs": 22.0},
    "红薯": {"calories": 86, "protein": 1.6, "fat": 0.1, "carbs": 20.0},
    "土豆": {"calories": 77, "protein": 2.0, "fat": 0.1, "carbs": 17.0},
    "粥": {"calories": 46, "protein": 1.1, "fat": 0.3, "carbs": 9.9},

    # 肉类
    "鸡胸肉": {"calories": 165, "protein": 31.0, "fat": 3.6, "carbs": 0},
    "鸡腿肉": {"calories": 177, "protein": 18.0, "fat": 11.0, "carbs": 0},
    "牛肉": {"calories": 250, "protein": 26.0, "fat": 15.0, "carbs": 0},
    "瘦牛肉": {"calories": 146, "protein": 26.0, "fat": 3.5, "carbs": 0},
    "猪肉": {"calories": 395, "protein": 13.0, "fat": 37.0, "carbs": 0},
    "瘦猪肉": {"calories": 143, "protein": 20.0, "fat": 6.0, "carbs": 0},
    "羊肉": {"calories": 292, "protein": 16.0, "fat": 24.0, "carbs": 0},
    "鱼肉": {"calories": 136, "protein": 20.0, "fat": 5.0, "carbs": 0},
    "三文鱼": {"calories": 208, "protein": 20.0, "fat": 13.0, "carbs": 0},
    "虾仁": {"calories": 99, "protein": 24.0, "fat": 0.3, "carbs": 0.2},
    "鸡蛋": {"calories": 155, "protein": 13.0, "fat": 11.0, "carbs": 1.1},

    # 蔬菜类
    "西兰花": {"calories": 34, "protein": 2.8, "fat": 0.4, "carbs": 7.0},
    "菠菜": {"calories": 23, "protein": 2.9, "fat": 0.4, "carbs": 3.6},
    "生菜": {"calories": 15, "protein": 1.4, "fat": 0.2, "carbs": 2.9},
    "西红柿": {"calories": 18, "protein": 0.9, "fat": 0.2, "carbs": 3.9},
    "黄瓜": {"calories": 15, "protein": 0.7, "fat": 0.1, "carbs": 3.6},
    "胡萝卜": {"calories": 41, "protein": 0.9, "fat": 0.2, "carbs": 10.0},
    "青椒": {"calories": 20, "protein": 0.9, "fat": 0.2, "carbs": 4.6},
    "茄子": {"calories": 25, "protein": 1.0, "fat": 0.2, "carbs": 6.0},
    "蘑菇": {"calories": 22, "protein": 3.1, "fat": 0.3, "carbs": 3.3},
    "白菜": {"calories": 16, "protein": 1.2, "fat": 0.2, "carbs": 3.0},
    "芹菜": {"calories": 16, "protein": 0.7, "fat": 0.2, "carbs": 3.0},
    "洋葱": {"calories": 40, "protein": 1.1, "fat": 0.1, "carbs": 9.0},

    # 水果类
    "苹果": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14.0},
    "香蕉": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23.0},
    "橙子": {"calories": 47, "protein": 0.9, "fat": 0.1, "carbs": 12.0},
    "葡萄": {"calories": 67, "protein": 0.6, "fat": 0.4, "carbs": 17.0},
    "草莓": {"calories": 32, "protein": 0.7, "fat": 0.3, "carbs": 7.7},
    "蓝莓": {"calories": 57, "protein": 0.7, "fat": 0.3, "carbs": 14.0},
    "西瓜": {"calories": 30, "protein": 0.6, "fat": 0.2, "carbs": 8.0},
    "梨": {"calories": 57, "protein": 0.4, "fat": 0.1, "carbs": 15.0},
    "猕猴桃": {"calories": 61, "protein": 1.1, "fat": 0.5, "carbs": 15.0},
    "芒果": {"calories": 60, "protein": 0.8, "fat": 0.4, "carbs": 15.0},

    # 奶制品
    "牛奶": {"calories": 42, "protein": 3.4, "fat": 1.0, "carbs": 5.0},
    "酸奶": {"calories": 59, "protein": 3.5, "fat": 0.4, "carbs": 10.0},
    "希腊酸奶": {"calories": 59, "protein": 10.0, "fat": 0.4, "carbs": 3.6},
    "奶酪": {"calories": 402, "protein": 25.0, "fat": 33.0, "carbs": 1.3},
    "低脂牛奶": {"calories": 34, "protein": 3.4, "fat": 0.2, "carbs": 5.0},

    # 豆制品
    "豆腐": {"calories": 76, "protein": 8.0, "fat": 4.8, "carbs": 1.9},
    "豆浆": {"calories": 33, "protein": 3.0, "fat": 1.6, "carbs": 1.7},
    "豆干": {"calories": 140, "protein": 16.0, "fat": 6.0, "carbs": 4.0},
    "毛豆": {"calories": 121, "protein": 11.0, "fat": 5.0, "carbs": 9.0},

    # 坚果类
    "杏仁": {"calories": 579, "protein": 21.0, "fat": 50.0, "carbs": 22.0},
    "核桃": {"calories": 654, "protein": 15.0, "fat": 65.0, "carbs": 14.0},
    "花生": {"calories": 567, "protein": 26.0, "fat": 49.0, "carbs": 16.0},
    "腰果": {"calories": 553, "protein": 18.0, "fat": 44.0, "carbs": 30.0},
    "开心果": {"calories": 560, "protein": 20.0, "fat": 45.0, "carbs": 27.0},

    # 调味和油脂
    "橄榄油": {"calories": 884, "protein": 0, "fat": 100.0, "carbs": 0},
    "食用油": {"calories": 884, "protein": 0, "fat": 100.0, "carbs": 0},
    "黄油": {"calories": 717, "protein": 0.9, "fat": 81.0, "carbs": 0.1},
    "蜂蜜": {"calories": 304, "protein": 0.3, "fat": 0, "carbs": 82.0},
    "白糖": {"calories": 387, "protein": 0, "fat": 0, "carbs": 100.0},
    "酱油": {"calories": 53, "protein": 8.0, "fat": 0, "carbs": 5.0},
}

# 食物分类用于浏览
FOOD_CATEGORIES = {
    "主食": ["米饭", "馒头", "面条", "面包", "燕麦", "玉米", "红薯", "土豆", "粥"],
    "肉类": ["鸡胸肉", "鸡腿肉", "牛肉", "瘦牛肉", "猪肉", "瘦猪肉", "羊肉", "鱼肉", "三文鱼", "虾仁", "鸡蛋"],
    "蔬菜": ["西兰花", "菠菜", "生菜", "西红柿", "黄瓜", "胡萝卜", "青椒", "茄子", "蘑菇", "白菜", "芹菜", "洋葱"],
    "水果": ["苹果", "香蕉", "橙子", "葡萄", "草莓", "蓝莓", "西瓜", "梨", "猕猴桃", "芒果"],
    "奶制品": ["牛奶", "酸奶", "希腊酸奶", "奶酪", "低脂牛奶"],
    "豆制品": ["豆腐", "豆浆", "豆干", "毛豆"],
    "坚果": ["杏仁", "核桃", "花生", "腰果", "开心果"],
    "调味": ["橄榄油", "食用油", "黄油", "蜂蜜", "白糖", "酱油"],
}


def search_food(query: str) -> list:
    """搜索食物"""
    results = []
    query = query.lower()
    for name, nutrition in FOOD_DATABASE.items():
        if query in name.lower():
            results.append({
                "name": name,
                **nutrition
            })
    return results


def get_food_names(category: str = None) -> list:
    """获取食物名称列表"""
    if category and category in FOOD_CATEGORIES:
        return FOOD_CATEGORIES[category]
    return list(FOOD_DATABASE.keys())
