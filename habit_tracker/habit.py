class Habit:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.streak = 0
        self.completed_dates = []

    def complete(self, date):
        self.completed_dates.append(date)
        self.streak += 1

    def __str__(self):
        return f"{self.name} (streak: {self.streak}) — {self.description}"