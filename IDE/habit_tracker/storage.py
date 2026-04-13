import json
import os
from habit import Habit

DATA_FILE = "habits.json"

def save_habits(habits):
    data = []
    for h in habits:
        data.append({
            "name": h.name,
            "description": h.description,
            "streak": h.streak,
            "completed_dates": h.completed_dates
        })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_habits():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    habits = []
    for item in data:
        h = Habit(item["name"], item["description"])
        h.streak = item["streak"]
        h.completed_dates = item["completed_dates"]
        habits.append(h)
    return habits