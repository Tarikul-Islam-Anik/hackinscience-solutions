import datetime


def friday_the_13th():
    date = datetime.date.today()
    while True:
        if date.day == 13 and date.weekday() == 4:
            return date.strftime("%Y-%m-%d")
        date += datetime.timedelta(days=1)
