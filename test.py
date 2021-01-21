from datetime import date
today = date.today()

td = today.strftime("%d.%m.%Y")
sample = "23.01.2021"

first = int(sample[:2])
second = int(td[:2])

print(first - second)
