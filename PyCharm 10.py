import datetime

date = list(map(int, input().split()))
date_day = int(input())

date_datetime = datetime.date(date[0], date[1], date[2])

date_timedelta = date_datetime + datetime.timedelta(days=date_day)

print(date_timedelta.year, date_timedelta.month, date_timedelta.day)



