"""
减脂期饮食管理软件 - 主程序
"""

from tracker import DietTracker, DailyRecord
from food_database import (
    FOOD_DATABASE,
    FOOD_CATEGORIES,
    search_food,
    get_food_names,
)


def print_header(title: str):
    """打印标题"""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)


def print_menu():
    """打印主菜单"""
    print_header("🥗 减脂饮食管理")
    print("""
  1. 📝 记录饮食
  2. 📊 查看今日摄入
  3. 📅 查看指定日期记录
  4. 🔍 查询食物营养
  5. 📈 查看食物分类
  6. ⚙️  设置每日目标
  7. 💾 保存并退出
    """)


def record_food(tracker: DietTracker):
    """记录饮食"""
    print_header("📝 记录饮食")

    # 选择餐次
    meal_types = {
        "1": "breakfast",
        "2": "lunch",
        "3": "dinner",
        "4": "snack",
    }
    print("\n选择餐次:")
    print("  1. 早餐  2. 午餐  3. 晚餐  4. 加餐")

    meal_choice = input("请输入餐次编号 (1-4): ").strip()
    meal_type = meal_types.get(meal_choice, "lunch")
    meal_name = {"breakfast": "早餐", "lunch": "午餐", "dinner": "晚餐", "snack": "加餐"}[meal_type]

    # 搜索食物
    query = input("\n请输入食物名称（或输入 browse 浏览分类）: ").strip()

    if query.lower() == "browse":
        print("\n食物分类:")
        for i, (cat, foods) in enumerate(FOOD_CATEGORIES.items(), 1):
            print(f"  {i}. {cat}")

        cat_choice = input("请选择分类编号: ").strip()
        try:
            cat_name = list(FOOD_CATEGORIES.keys())[int(cat_choice) - 1]
            foods = FOOD_CATEGORIES[cat_name]
            print(f"\n【{cat_name}】包含的食物:")
            for i, food in enumerate(foods, 1):
                print(f"  {i}. {food}")
            food_choice = input("请选择食物编号: ").strip()
            query = foods[int(food_choice) - 1]
        except (ValueError, IndexError):
            print("无效的选择")
            return

    # 查找食物
    results = search_food(query)
    if not results:
        print(f"未找到包含 '{query}' 的食物")
        return

    print(f"\n找到 {len(results)} 个匹配的食物:")
    for i, food in enumerate(results[:10], 1):
        print(
            f"  {i}. {food['name']} - "
            f"{food['calories']}kcal/100g "
            f"(P:{food['protein']}g F:{food['fat']}g C:{food['carbs']}g)"
        )

    if len(results) > 10:
        print("  ... 更多结果请缩小搜索范围")

    choice = input("\n请选择食物编号: ").strip()
    try:
        selected = results[int(choice) - 1]
    except (ValueError, IndexError):
        print("无效的选择")
        return

    # 输入重量
    weight = input(f"请输入 '{selected['name']}' 的重量 (克): ").strip()
    try:
        weight = float(weight)
        if weight <= 0:
            raise ValueError()
    except ValueError:
        print("请输入有效的重量")
        return

    # 添加记录
    entry = tracker.add_food(selected["name"], weight, meal_type)
    if entry:
        print(
            f"\n✅ 已添加：{selected['name']} {weight}g ({entry.nutrition['calories']} kcal)"
        )
        print(
            f"   蛋白质:{entry.nutrition['protein']}g | "
            f"脂肪:{entry.nutrition['fat']}g | "
            f"碳水:{entry.nutrition['carbs']}g"
        )


def view_today(tracker: DietTracker):
    """查看今日摄入"""
    print_header("📊 今日摄入")
    report = tracker.get_daily_report()
    print(report)

    # 显示目标对比
    totals = tracker.get_or_create_record().get_totals()
    print(f"\n{'-'*50}")
    print("💡 提示：正常成年人每日建议摄入:")
    print("   热量：1800-2200 kcal (减脂期建议 1200-1600)")
    print("   蛋白质：50-70g")
    print("   脂肪：50-70g")
    print("   碳水：200-300g")


def view_date(tracker: DietTracker):
    """查看指定日期记录"""
    date = input("请输入日期 (YYYY-MM-DD): ").strip()
    report = tracker.get_daily_report(date)
    print_header(f"📅 {date} 的饮食记录")
    print(report)


def search_food_view():
    """查询食物营养"""
    print_header("🔍 查询食物营养")
    query = input("请输入食物名称: ").strip()
    results = search_food(query)

    if not results:
        print(f"未找到包含 '{query}' 的食物")
        return

    print(f"\n找到 {len(results)} 个匹配结果:")
    print("-" * 60)
    print(f"{'食物名称':<10} {'热量':<10} {'蛋白质':<8} {'脂肪':<8} {'碳水':<8}")
    print("-" * 60)

    for food in results:
        print(
            f"{food['name']:<10} {food['calories']:<10} "
            f"{food['protein']:<8} {food['fat']:<8} {food['carbs']:<8}"
        )

    print("-" * 60)
    print("注：以上数据均为每 100g 可食部分的含量")


def view_categories():
    """查看食物分类"""
    print_header("📈 食物分类")

    for category, foods in FOOD_CATEGORIES.items():
        print(f"\n【{category}】")
        for food in foods:
            data = FOOD_DATABASE[food]
            print(
                f"  {food:<10} {data['calories']}kcal  "
                f"P:{data['protein']}g F:{data['fat']}g C:{data['carbs']}g"
            )


def main():
    """主程序"""
    tracker = DietTracker()

    while True:
        print_menu()
        choice = input("请选择功能 (1-7): ").strip()

        if choice == "1":
            record_food(tracker)
        elif choice == "2":
            view_today(tracker)
        elif choice == "3":
            view_date(tracker)
        elif choice == "4":
            search_food_view()
        elif choice == "5":
            view_categories()
        elif choice == "6":
            print("⚙️  目标设置功能开发中...")
        elif choice == "7":
            tracker.save_data()
            print("\n✅ 数据已保存，感谢使用！")
            print("  祝您减脂成功！💪\n")
            break
        else:
            print("无效的选择，请重新输入")

        input("\n按回车键继续...")


if __name__ == "__main__":
    main()
