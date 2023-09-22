from datetime import datetime
year=datetime.today().year
month=datetime.today().month
day=datetime.today().day
hour=datetime.today().hour
if hour + 9 > 24:
    day = day + 1
if datetime.today().month > 9:
    print(f"{year}-{month}-{day}")
else:
    print(f"{year}-0{month}-{day}")