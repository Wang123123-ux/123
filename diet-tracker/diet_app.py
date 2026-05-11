"""
减脂期饮食管理软件 - GUI 版本
使用 tkinter 图形界面，双击即可运行
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

# ============== 食物数据库 ==============
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

FOOD_CATEGORIES = {
    "全部": list(FOOD_DATABASE.keys()),
    "主食": ["米饭", "馒头", "面条", "面包", "燕麦", "玉米", "红薯", "土豆", "粥"],
    "肉类": ["鸡胸肉", "鸡腿肉", "牛肉", "瘦牛肉", "猪肉", "瘦猪肉", "鱼肉", "三文鱼", "虾仁", "鸡蛋"],
    "蔬菜": ["西兰花", "菠菜", "生菜", "西红柿", "黄瓜", "胡萝卜", "青椒", "茄子", "蘑菇", "白菜", "芹菜", "洋葱"],
    "水果": ["苹果", "香蕉", "橙子", "葡萄", "草莓", "蓝莓", "西瓜", "梨", "猕猴桃", "芒果"],
    "奶制品": ["牛奶", "酸奶", "希腊酸奶", "奶酪", "低脂牛奶"],
    "豆制品": ["豆腐", "豆浆", "豆干", "毛豆"],
    "坚果": ["杏仁", "核桃", "花生", "腰果", "开心果"],
    "调味": ["橄榄油", "食用油", "黄油", "蜂蜜", "白糖", "酱油"],
}

MEAL_NAMES = {
    "breakfast": "🌅 早餐",
    "lunch": "☀️ 午餐",
    "dinner": "🌙 晚餐",
    "snack": "🍪 加餐",
}


class DietTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🥗 减脂饮食管理")
        self.root.geometry("900x650")
        self.root.minsize(800, 600)

        self.data_file = os.path.join(os.path.dirname(__file__), "diet_data.json")
        self.records = self.load_data()
        self.current_date = datetime.now().strftime("%Y-%m-%d")

        self.setup_ui()
        self.refresh_display()

    def load_data(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)

    def setup_ui(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 顶部：日期选择和今日概览
        top_frame = ttk.LabelFrame(main_frame, text="📅 今日概览", padding="10")
        top_frame.pack(fill=tk.X, pady=(0, 10))

        # 日期选择
        date_frame = ttk.Frame(top_frame)
        date_frame.pack(fill=tk.X)

        ttk.Label(date_frame, text="日期:").pack(side=tk.LEFT)
        self.date_var = tk.StringVar(value=self.current_date)
        self.date_entry = ttk.Entry(date_frame, textvariable=self.date_var, width=12)
        self.date_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(date_frame, text="查看", command=self.refresh_display).pack(side=tk.LEFT)
        ttk.Button(date_frame, text="今天", command=self.go_to_today).pack(side=tk.LEFT, padx=5)

        # 今日总计标签
        self.summary_label = ttk.Label(top_frame, text="", font=("", 12))
        self.summary_label.pack(fill=tk.X, pady=(10, 0))

        # 进度条
        self.progress_frame = ttk.Frame(top_frame)
        self.progress_frame.pack(fill=tk.X, pady=(5, 0))

        ttk.Label(self.progress_frame, text="热量摄入进度:").pack(anchor=tk.W)
        self.calorie_progress = ttk.Progressbar(self.progress_frame, length=400, mode="determinate")
        self.calorie_progress.pack(fill=tk.X)

        # 中部：左侧添加食物，右侧记录列表
        mid_frame = ttk.Frame(main_frame)
        mid_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # 左侧：添加食物
        left_frame = ttk.LabelFrame(mid_frame, text="📝 添加食物", padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # 餐次选择
        ttk.Label(left_frame, text="餐次:").pack(anchor=tk.W)
        self.meal_var = tk.StringVar(value="breakfast")
        meal_combo = ttk.Combobox(left_frame, textvariable=self.meal_var, values=list(MEAL_NAMES.values()), state="readonly")
        meal_combo.pack(fill=tk.X, pady=(0, 10))
        meal_combo.current(0)

        # 分类选择
        ttk.Label(left_frame, text="分类:").pack(anchor=tk.W)
        self.category_var = tk.StringVar(value="全部")
        category_combo = ttk.Combobox(left_frame, textvariable=self.category_var, values=list(FOOD_CATEGORIES.keys()), state="readonly")
        category_combo.pack(fill=tk.X, pady=(0, 10))
        category_combo.bind("<<ComboboxSelected>>", self.on_category_change)

        # 食物选择
        ttk.Label(left_frame, text="食物:").pack(anchor=tk.W)
        self.food_var = tk.StringVar()
        self.food_combo = ttk.Combobox(left_frame, textvariable=self.food_var, state="readonly")
        self.food_combo.pack(fill=tk.X, pady=(0, 10))

        # 营养预览（在 update_food_list 之前初始化）
        self.preview_label = ttk.Label(left_frame, text="", foreground="gray")
        self.preview_label.pack(fill=tk.X, pady=(0, 10))

        self.update_food_list()

        # 重量输入
        ttk.Label(left_frame, text="重量 (克):").pack(anchor=tk.W)
        self.weight_var = tk.StringVar(value="100")
        weight_entry = ttk.Entry(left_frame, textvariable=self.weight_var)
        weight_entry.pack(fill=tk.X, pady=(0, 10))

        # 营养预览
        self.preview_label = ttk.Label(left_frame, text="", foreground="gray")
        self.preview_label.pack(fill=tk.X, pady=(0, 10))

        # 添加按钮
        ttk.Button(left_frame, text="➕ 添加记录", command=self.add_food).pack(fill=tk.X)

        # 右侧：今日记录
        right_frame = ttk.LabelFrame(mid_frame, text="📋 今日记录", padding="10")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # 记录列表
        columns = ("food", "weight", "meal", "calories", "protein", "fat", "carbs")
        self.record_tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=10)

        self.record_tree.heading("food", text="食物")
        self.record_tree.heading("weight", text="重量")
        self.record_tree.heading("meal", text="餐次")
        self.record_tree.heading("calories", text="热量")
        self.record_tree.heading("protein", text="蛋白质")
        self.record_tree.heading("fat", text="脂肪")
        self.record_tree.heading("carbs", text="碳水")

        self.record_tree.column("food", width=80)
        self.record_tree.column("weight", width=50)
        self.record_tree.column("meal", width=50)
        self.record_tree.column("calories", width=50)
        self.record_tree.column("protein", width=50)
        self.record_tree.column("fat", width=50)
        self.record_tree.column("carbs", width=50)

        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.record_tree.yview)
        self.record_tree.configure(yscrollcommand=scrollbar.set)

        self.record_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 删除按钮
        ttk.Button(right_frame, text="🗑️ 删除选中", command=self.delete_selected).pack(fill=tk.X, pady=(5, 0))

        # 底部：宏量营养分布
        bottom_frame = ttk.LabelFrame(main_frame, text="💪 宏量营养分布", padding="10")
        bottom_frame.pack(fill=tk.X)

        self.macro_label = ttk.Label(bottom_frame, text="", font=("", 11))
        self.macro_label.pack()

    def update_food_list(self, event=None):
        category = self.category_var.get()
        foods = FOOD_CATEGORIES.get(category, list(FOOD_DATABASE.keys()))
        self.food_combo["values"] = foods
        if foods:
            self.food_combo.current(0)
            self.update_preview()

    def on_category_change(self, event):
        self.update_food_list()

    def update_preview(self, event=None):
        food_name = self.food_var.get()
        if food_name in FOOD_DATABASE:
            data = FOOD_DATABASE[food_name]
            self.preview_label.config(
                text=f"每 100g: {data['calories']}大卡 | 蛋白质:{data['protein']}g | 脂肪:{data['fat']}g | 碳水:{data['carbs']}g"
            )

    def get_meal_key(self, meal_name):
        for key, name in MEAL_NAMES.items():
            if name == meal_name:
                return key
        return "lunch"

    def add_food(self):
        food_name = self.food_var.get()
        meal_name = self.meal_var.get()
        weight_str = self.weight_var.get()

        if not food_name:
            messagebox.showwarning("提示", "请选择食物")
            return

        try:
            weight = float(weight_str)
            if weight <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showwarning("提示", "请输入有效的重量")
            return

        meal_key = self.get_meal_key(meal_name)
        date = self.date_var.get()

        if date not in self.records:
            self.records[date] = {"entries": []}

        # 计算营养
        data = FOOD_DATABASE[food_name]
        factor = weight / 100.0
        nutrition = {
            "calories": round(data["calories"] * factor, 1),
            "protein": round(data["protein"] * factor, 1),
            "fat": round(data["fat"] * factor, 1),
            "carbs": round(data["carbs"] * factor, 1),
        }

        entry = {
            "name": food_name,
            "weight": weight,
            "meal_type": meal_key,
            "nutrition": nutrition,
        }

        self.records[date]["entries"].append(entry)
        self.save_data()
        self.refresh_display()

        messagebox.showinfo("成功", f"已添加：{food_name} {weight}g ({nutrition['calories']}大卡)")

    def delete_selected(self):
        selected = self.record_tree.selection()
        if not selected:
            messagebox.showwarning("提示", "请先选择要删除的记录")
            return

        indices = sorted([int(self.record_tree.item(item)["values"][0]) for item in selected], reverse=True)
        date = self.date_var.get()

        if date in self.records:
            for idx in indices:
                if 0 <= idx < len(self.records[date]["entries"]):
                    del self.records[date]["entries"][idx]

            self.save_data()
            self.refresh_display()

    def calculate_totals(self):
        date = self.date_var.get()
        totals = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}

        if date in self.records:
            for entry in self.records[date].get("entries", []):
                nutrition = entry.get("nutrition", {})
                totals["calories"] += nutrition.get("calories", 0)
                totals["protein"] += nutrition.get("protein", 0)
                totals["fat"] += nutrition.get("fat", 0)
                totals["carbs"] += nutrition.get("carbs", 0)

        return {k: round(v, 1) for k, v in totals.items()}

    def refresh_display(self):
        date = self.date_var.get()

        # 清空列表
        for item in self.record_tree.get_children():
            self.record_tree.delete(item)

        # 填充记录
        if date in self.records:
            for idx, entry in enumerate(self.records[date].get("entries", [])):
                meal_name = MEAL_NAMES.get(entry["meal_type"], entry["meal_type"])
                nutrition = entry.get("nutrition", {})
                self.record_tree.insert("", tk.END, values=(
                    idx,
                    entry["name"],
                    f"{entry['weight']}g",
                    meal_name,
                    nutrition.get("calories", 0),
                    nutrition.get("protein", 0),
                    nutrition.get("fat", 0),
                    nutrition.get("carbs", 0),
                ))

        # 更新总计
        totals = self.calculate_totals()
        self.summary_label.config(
            text=f"🔥 热量：{totals['calories']} 大卡  |  "
                 f"💪 蛋白质：{totals['protein']}g  |  "
                 f"🥑 脂肪：{totals['fat']}g  |  "
                 f"🍚 碳水：{totals['carbs']}g"
        )

        # 更新进度条（以 1500 大卡为目标）
        progress = min((totals["calories"] / 1500) * 100, 100)
        self.calorie_progress["value"] = progress

        # 更新宏量显示
        # 计算宏量热量占比
        protein_cal = totals["protein"] * 4
        fat_cal = totals["fat"] * 9
        carbs_cal = totals["carbs"] * 4
        total_macro_cal = protein_cal + fat_cal + carbs_cal

        if total_macro_cal > 0:
            protein_pct = protein_cal / total_macro_cal * 100
            fat_pct = fat_cal / total_macro_cal * 100
            carbs_pct = carbs_cal / total_macro_cal * 100

            self.macro_label.config(
                text=f"蛋白质：{totals['protein']}g ({protein_pct:.0f}%)  |  "
                     f"脂肪：{totals['fat']}g ({fat_pct:.0f}%)  |  "
                     f"碳水：{totals['carbs']}g ({carbs_pct:.0f}%)"
            )
        else:
            self.macro_label.config(text="暂无数据")

    def go_to_today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        self.date_var.set(today)
        self.refresh_display()


def main():
    root = tk.Tk()
    app = DietTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
