import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date

today = date.today()
today = today.strftime("%d.%m.%Y")

td = int(today[:2])

def naruto():
    # opening browser with certain site
    driver = webdriver.Chrome()
    driver.get("https://naruto.wbijam.pl/")

    # searching for date
    table = driver.find_element_by_class_name("lista")
    dates = table.find_elements_by_class_name("lista_td")

    # searching for results
    results = table.find_elements_by_class_name("lista_td_calendar")

    time = []

    n = len(dates) - 1

    for i in range(n):
        temp = dates[i].text
        txt = results[i].text
        time.append([int(temp[:2]), txt])

    for day, result in time:
        sub = day - td
        if sub == 0 and result == "zakończony":
            print("Go watch now!")
        elif sub == 0:
            print("Today is a day!")
        else:
            print("Not today :(")
            break

#    # collecting dates
#    for date in dates:
#        temp = date.text
#        time_str.append(temp[:2])
#
#    # converting string list to int list
#    time = list(map(int, time_str))
#
#    # checking if today is a day
#
#    for day in time:
#        result = day - td
#        if result == 0 and :
#            print("Today is a day")
    
    driver.quit()
naruto()

def drstone():
    driver = webdriver.Chrome()
    driver.get("https://drstone.wbijam.pl/#")

    table = driver.find_element_by_class_name("lista")
    dates = table.find_elements_by_class_name("lista_td_calendar")

    for date in dates:
        if date.text == "zakończony":
            continue
        print(date.text)
    driver.quit()    

