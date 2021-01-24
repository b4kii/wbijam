import time
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date

driver = webdriver.Chrome()
# waiting until the whole page is loaded
driver.implicitly_wait(10)
driver.get("https://blackclover.wbijam.pl/")

def check():
    # getting current date
    today = date.today()
    today = today.strftime("%d.%m.%Y")
    
    # getting day and month number from current date 
    td = today[:5]

    # searching for emission date
    table = driver.find_element_by_class_name("lista")
    dates = table.find_elements_by_class_name("lista_td")

    # handling error with upcoming series
    daty = []
    r = re.compile("^[\d]{1,2}[.][\d]{1,2}[.][\d]{4}")

    for dat in dates:
        if dat.text == "nadchodzi" or not r.match(dat.text):
            continue
        else:
            daty.append(dat.text)

    # searching for results
    results = table.find_elements_by_class_name("lista_td_calendar")

    time = []
    n = len(daty)
    temp = ""
    for i in range(n):
        if r.match(daty[i]):
            temp = daty[i]
        txt = results[i].text
        time.append([temp[:5], txt])

    noti = ""
    for day, result in time:
        if td == day:
            if result == "zakończony":
                noti = "Go watch now"
            elif result == "TŁUMACZENIE":
                noti = "Wait for the episode translation"
            else:
                noti = "Today is a day"
            break
        else:
            noti = "Not today"
    return noti

right = driver.find_element_by_id("menu_prawa")
lists = right.find_elements_by_tag_name("li")

n = len(lists) - 1
start, end = 0, 0
series, final = [], []

# searching for ongoing anime series
for i in range(n):
    if lists[i].text == "Wychodzące/ongoing:":
        start = i + 1
    if lists[i].text == "Zakończone/wstrzymane:":
        end = i
for j in range(start, end):
    series.append(lists[j].text)

# accepting privacy settings
rodo = driver.find_element_by_class_name("details_save--3nDG7")
rodo.click()
# accepting cookies
cookie = driver.find_element_by_id("simplecookienotificationokbutton")
cookie.click()

# final loop
for serie in series:
    link = driver.find_element_by_link_text(serie)
    link.click()
    time.sleep(5)
    ch = check()
    final.append([serie, ch])
    time.sleep(10)

# some pretty display format
s = [[str(e) for e in row] for row in final]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))

