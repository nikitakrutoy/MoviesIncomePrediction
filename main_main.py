from selenium import webdriver
import requests
from itertools import cycle
import time
import csv
import random
from selenium.common.exceptions import NoSuchElementException


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

chromedriver_location = "/Users/sergeyone/Downloads/chromedriver-2"
driver = webdriver.Chrome(chromedriver_location)

with open('id_list_2015.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
    for row in spamreader:
        id = str(row[0])
        print(id)
        #открываем сайт
        driver.get('https://www.kinopoisk.ru/film/' + id + '/')
        date_world = '//*[@id="div_world_prem_td2"]/div/a[1]'
        date_rus = '//*[@id="div_rus_prem_td2"]/div/span/a[1]'
        viewers = '//*[@id="infoTable"]/table/tbody/tr[15]/td[2]/div/div'
        viewers_country = '//*[@id="infoTable"]/table/tbody/tr[16]/td[2]/div/div/img[]/title'
        budget = '//*[@id="infoTable"]/table/tbody/tr[12]/td[2]/div'
        age_select = '//*[@id="infoTable"]/table/tbody/tr[22]/td[1]'
        age = '//*[@id="infoTable"]/table/tbody/tr[22]/td[2]/span'

        dw = "None"
        dr = "None"
        vw = "None"
        bg = "None"
        ag = "None"
        vc = "None"

        if check_exists_by_xpath(date_world) == True:
            dw = driver.find_element_by_xpath(date_world).text
        if check_exists_by_xpath(date_rus) == True:
            dr = driver.find_element_by_xpath(date_rus).text
        if check_exists_by_xpath(viewers) == True:
            vw = driver.find_element_by_xpath(viewers).text
        if check_exists_by_xpath(budget) == True:
            bg = driver.find_element_by_xpath(budget).text
        if check_exists_by_xpath(viewers_country) == True:
            vc = driver.find_element_by_xpath(viewers_country).text

        if check_exists_by_xpath(age) == True:
            try:
                driver.find_element_by_xpath(age_select).click()
            except:
                print('Nope')
            ag = driver.find_element_by_xpath(age).text
            print(ag)
            print(vc)

        with open('dates_2015_left.csv', 'a', newline='', encoding='utf-8') as csvfile:

            spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([str(id)] + [str(dw)] + [str(dr)]+ [str(vc + ' : ' + vw)] + [str(bg)] + [str(ag)])
            print([str(id)] + [str(dw)] + [str(dr)] + [str(vw)] + [str(bg)] + [str(ag)])
        time.sleep(random.uniform(0, 30))




'''
        #ищем поля
        inn_filed = '//*[@id="content"]/form/table/tbody/tr/td[1]/table/tbody/tr[2]/td[1]/input'
        # driver.find_element_by_xpath(inn).click()
        time.sleep(random.uniform(0, 3))
        submit_button = '//*[@id="content"]/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td/button'
        print("a" + str(inn_company))
        # вводим ИНН
        driver.find_element_by_xpath(inn_filed).send_keys(inn_company)
        #отправляем
        driver.find_element_by_xpath(submit_button).click()
'''
''' 
        #заходим в каротчку, проверяя, что она существует
        if check_exists_by_xpath('//*[@id="content"]/table[1]/tbody/tr/td[2]/a') == True:
            time.sleep(random.uniform(0, 30))
            company_card = '//*[@id="content"]/table[1]/tbody/tr/td[2]/a'
            driver.find_element_by_xpath(company_card).click()
            #находим челика
            name_resp = '//*[@id="content"]/table[1]/tbody/tr[11]/td[2]'
            contact_resp = '//*[@id="content"]/table[1]/tbody/tr[12]/td[2]'
            #записываем челика в переменную
            name_resp_text = "None"
            contact_resp_text = "None"
            if check_exists_by_xpath(name_resp) == True:
                name_resp_text = driver.find_element_by_xpath(name_resp).text
            if check_exists_by_xpath(contact_resp) == True:
                contact_resp_text = driver.find_element_by_xpath(contact_resp).text

            with open('contacts.csv', 'a', newline='', encoding='utf-8') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([str(inn_company)]+[str(name_resp_text)]+[str(contact_resp_text)])
                print([str(inn_company)]+[str(name_resp_text)]+[str(contact_resp_text)])

            a = a + 1
            print("done: " + str(a) + " rows")
            time.sleep(random.uniform(0, 10))
print ('done everything')
'''