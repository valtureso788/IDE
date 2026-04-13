from habit import Habit
from storage import save_habits, load_habits
from utils import today_str, display_habits

def main():
    habits = load_habits()
    today = today_str()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Показать привычки")
        print("2. Добавить привычку")
        print("3. Отметить выполнение")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_habits(habits)

        elif choice == "2":
            name = input("Название привычки: ")
            desc = input("Описание: ")
            habits.append(Habit(name, desc))
            save_habits(habits)
            print("Привычка добавлена!")

        elif choice == "3":
            display_habits(habits)
            try:
                idx = int(input("Номер привычки: ")) - 1
                if 0 <= idx < len(habits):
                    habits[idx].complete(today)
                    save_habits(habits)
                    print("Отмечено!")
                else:
                    print("Неверный номер")
            except ValueError:
                print("Введите число")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()