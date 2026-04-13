from datetime import date

def today_str():
    return str(date.today())

def display_habits(habits):
    if not habits:
        print("Нет привычек.")
        return
    for i, h in enumerate(habits, 1):
        print(f"{i}. {h}")
