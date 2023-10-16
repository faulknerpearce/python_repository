class Weekday:
    
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __repr__(self):
        return f"This object belogs to the weekday class. it will return a string containing the day of the week that is currently is. "

    def get_weekday(self):
        from datetime import datetime
        current_time = datetime.now()
        weekday = current_time.weekday()
        return self.days[weekday]

today = Weekday()
print(today.get_weekday())