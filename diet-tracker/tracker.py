"""
饮食追踪器核心模块
记录和管理每日饮食摄入
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from food_database import FOOD_DATABASE


class FoodEntry:
    """单次食物摄入记录"""

    def __init__(self, name: str, weight: float, meal_type: str):
        self.name = name
        self.weight = weight  # 克
        self.meal_type = meal_type  # breakfast, lunch, dinner, snack
        self.nutrition = self._calculate_nutrition()

    def _calculate_nutrition(self) -> Dict:
        """计算该次摄入的营养"""
        if self.name not in FOOD_DATABASE:
            return {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}

        base = FOOD_DATABASE[self.name]
        factor = self.weight / 100.0

        return {
            "calories": round(base["calories"] * factor, 1),
            "protein": round(base["protein"] * factor, 1),
            "fat": round(base["fat"] * factor, 1),
            "carbs": round(base["carbs"] * factor, 1),
        }

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "weight": self.weight,
            "meal_type": self.meal_type,
            "nutrition": self.nutrition,
        }


class DailyRecord:
    """每日饮食记录"""

    MEAL_NAMES = {
        "breakfast": "早餐",
        "lunch": "午餐",
        "dinner": "晚餐",
        "snack": "加餐",
    }

    def __init__(self, date: str = None):
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.entries: List[FoodEntry] = []

    def add_food(
        self, name: str, weight: float, meal_type: str = "lunch"
    ) -> Optional[FoodEntry]:
        """添加食物记录"""
        if name not in FOOD_DATABASE:
            return None

        entry = FoodEntry(name, weight, meal_type)
        self.entries.append(entry)
        return entry

    def remove_entry(self, index: int) -> bool:
        """删除记录"""
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
            return True
        return False

    def get_totals(self) -> Dict:
        """获取每日总摄入"""
        totals = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
        for entry in self.entries:
            for key in totals:
                totals[key] += entry.nutrition[key]

        return {k: round(v, 1) for k, v in totals.items()}

    def get_meal_totals(self, meal_type: str) -> Dict:
        """获取某餐的总摄入"""
        totals = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
        for entry in self.entries:
            if entry.meal_type == meal_type:
                for key in totals:
                    totals[key] += entry.nutrition[key]

        return {k: round(v, 1) for k, v in totals.items()}

    def get_entries_by_meal(self) -> Dict[str, List]:
        """按餐次分组返回记录"""
        result = {"breakfast": [], "lunch": [], "dinner": [], "snack": []}
        for entry in self.entries:
            result[entry.meal_type].append(entry.to_dict())
        return result

    def to_dict(self) -> Dict:
        return {
            "date": self.date,
            "entries": [e.to_dict() for e in self.entries],
            "totals": self.get_totals(),
        }

    def __str__(self) -> str:
        """格式化输出每日记录"""
        lines = [f"\n{'='*50}", f"📅 {self.date}", f"{'='*50}"]

        for meal_type, meal_name in self.MEAL_NAMES.items():
            meal_entries = [
                e for e in self.entries if e.meal_type == meal_type
            ]
            if meal_entries:
                lines.append(f"\n【{meal_name}】")
                for entry in meal_entries:
                    lines.append(
                        f"  • {entry.name} {entry.weight}g - "
                        f"{entry.nutrition['calories']} kcal "
                        f"(P:{entry.nutrition['protein']}g "
                        f"F:{entry.nutrition['fat']}g "
                        f"C:{entry.nutrition['carbs']}g)"
                    )

        totals = self.get_totals()
        lines.append(f"\n{'-'*50}")
        lines.append(f"【今日总计】")
        lines.append(
            f"  🔥 热量：{totals['calories']} kcal"
        )
        lines.append(
            f"  💪 蛋白质：{totals['protein']}g | "
            f"  🥑 脂肪：{totals['fat']}g | "
            f"  🍚 碳水：{totals['carbs']}g"
        )

        return "\n".join(lines)


class DietTracker:
    """饮食追踪器主类"""

    def __init__(self, data_file: str = "diet_data.json"):
        self.data_file = data_file
        self.records: Dict[str, DailyRecord] = {}
        self.load_data()

    def load_data(self):
        """加载数据"""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for date_str, record_data in data.items():
                    record = DailyRecord(date_str)
                    for entry_data in record_data.get("entries", []):
                        entry = FoodEntry(
                            entry_data["name"],
                            entry_data["weight"],
                            entry_data["meal_type"],
                        )
                        record.entries.append(entry)
                    self.records[date_str] = record
        except FileNotFoundError:
            pass

    def save_data(self):
        """保存数据"""
        data = {}
        for date_str, record in self.records.items():
            data[date_str] = record.to_dict()

        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_or_create_record(self, date: str = None) -> DailyRecord:
        """获取或创建某日的记录"""
        date = date or datetime.now().strftime("%Y-%m-%d")
        if date not in self.records:
            self.records[date] = DailyRecord(date)
        return self.records[date]

    def add_food(
        self,
        name: str,
        weight: float,
        meal_type: str = "lunch",
        date: str = None,
    ) -> Optional[FoodEntry]:
        """添加食物记录"""
        record = self.get_or_create_record(date)
        entry = record.add_food(name, weight, meal_type)
        if entry:
            self.save_data()
        return entry

    def get_daily_report(self, date: str = None) -> str:
        """获取每日报告"""
        date = date or datetime.now().strftime("%Y-%m-%d")
        if date not in self.records:
            return f"{date} 暂无饮食记录"
        return str(self.records[date])

    def get_weekly_summary(self, end_date: str = None) -> Dict:
        """获取周总结"""
        if not end_date:
            end_date = datetime.now().strftime("%Y-%m-%d")

        end = datetime.strptime(end_date, "%Y-%m-%d")
        summary = {
            "days": 0,
            "avg_calories": 0,
            "avg_protein": 0,
            "avg_fat": 0,
            "avg_carbs": 0,
            "total_calories": 0,
        }

        for i in range(7):
            date = (end - timedelta(days=i)).strftime("%Y-%m-%d")
            if date in self.records:
                totals = self.records[date].get_totals()
                summary["days"] += 1
                summary["total_calories"] += totals["calories"]
                summary["avg_protein"] += totals["protein"]
                summary["avg_fat"] += totals["fat"]
                summary["avg_carbs"] += totals["carbs"]

        if summary["days"] > 0:
            summary["avg_calories"] = round(
                summary["total_calories"] / summary["days"], 1
            )
            summary["avg_protein"] = round(
                summary["avg_protein"] / summary["days"], 1
            )
            summary["avg_fat"] = round(
                summary["avg_fat"] / summary["days"], 1
            )
            summary["avg_carbs"] = round(
                summary["avg_carbs"] / summary["days"], 1
            )

        return summary


# 需要导入 timedelta
from datetime import timedelta
