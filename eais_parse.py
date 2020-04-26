import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import random
import csv


new_df = pd.DataFrame()

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

chromedriver_location = "/Users/sergeyone/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver_location)

driver.get('http://ekinobilet.fond-kino.ru/statistics/')
choose_period = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[7]/div/span[1]'
choose_weekend = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[7]/div/span[1]/span/ul/li[2]'
table_path = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div'
#table_path = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div'
date_path = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[7]/div/span[2]/span[2]'
el_path = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div/div[11]'
rev_path = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[2]/a'
choose_previous = '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[7]/div/span[2]/span[1]'
try:
    time.sleep(random.uniform(5, 10))
    driver.find_element_by_xpath(choose_period).click()
    time.sleep(random.uniform(5, 10))
    driver.find_element_by_xpath(choose_weekend).click()
except:
    print('Nope')

driver.find_element_by_xpath(choose_previous).click()
for i in range(0,99999998):
    try:
        with open('EAIS_DB_v0.1.csv', 'a', newline='', encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #try:
            print('----//----')
            print('Weekend num: ' + str(i))
            driver.find_element_by_xpath(choose_previous).click()
      #  try:
      #      driver.find_element_by_xpath('//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[2]').click()
      #      driver.find_element_by_xpath(
      #          '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[2]').click()
      #  except:
      #      print('Нет такой')
            time.sleep(random.uniform(5, 10))
            a = driver.find_element_by_xpath(table_path).text
            print(a)
            aa = a.split('\n')
            b = driver.find_element_by_xpath(date_path).text
            print(b)
            print(aa)
            if len(aa) > 7:
                b = driver.find_element_by_xpath(date_path).text
                c = ((len(aa) - 1) / 8)
                print(',.,.,.,.')
                print(len(aa))
                print(c)
                print(',.,.,.,.')
                for ii in range(0, int(c)):
                    spamwriter.writerow([str(b)] + [str(aa[0+(8*ii)])] + [str(aa[1+(8*ii)])] +
                                      [str(aa[2+(8*ii)])] + [str(aa[3+(8*ii)])] +
                                      [str(aa[4+(8*ii)])] +
                                      [str(aa[5+(8*ii)])] + [str(aa[6+(8*ii)])] + [str(aa[7+(8*ii)])])

                    print([str(b)] + [str(aa[0+(8*ii)])] + [str(aa[1+(8*ii)])] +
                                      [str(aa[2+(8*ii)])] + [str(aa[3+(8*ii)])] +
                                      [str(aa[4+(8*ii)])] +
                                      [str(aa[5+(8*ii)])] + [str(aa[6+(8*ii)])] + [str(aa[7+(8*ii)])])


            driver.find_element_by_xpath(rev_path).click()
            time.sleep(random.uniform(4, 6))
            a = driver.find_element_by_xpath(table_path).text
            aa = a.split('\n')
            b = driver.find_element_by_xpath(date_path).text

            if len(aa) > 7:
                b = driver.find_element_by_xpath(date_path).text
                c = ((len(aa) - 1) / 8)
                for ii in range(0, int(c)):
                   spamwriter.writerow([str(b)] + [str(aa[0 + (8 * ii)])] + [str(aa[1 + (8 * ii)])] +
                   [str(aa[2 + (8 * ii)])] + [str(aa[3 + (8 * ii)])] +
                   [str(aa[4 + (8 * ii)])] +
                   [str(aa[5 + (8 * ii)])] + [str(aa[6 + (8 * ii)])] + [str(aa[7 + (8 * ii)])])

                   print([str(b)] + [str(aa[0 + (8 * ii)])] + [str(aa[1 + (8 * ii)])] +
                   [str(aa[2 + (8 * ii)])] + [str(aa[3 + (8 * ii)])] +
                   [str(aa[4 + (8 * ii)])] +
                   [str(aa[5 + (8 * ii)])] + [str(aa[6 + (8 * ii)])] + [str(aa[7 + (8 * ii)])])
            print('Done (num: ' + str(i) + ')')
    except:
        print('Something went wrong')


'''
              #  try:
      #      driver.find_element_by_xpath('//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[2]').click()
      #      driver.find_element_by_xpath(
      #          '//*[@id="main-wrap-inner"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/div/div[2]').click()
      #  except:
      #      print('Нет такой')
            if len(aa)>7:
                c = (len(aa)/8)
                print(c)
                for ii in range(0,int(c)):
                    spamwriter.writerow([str(b)] + [str(aa[0*int(ii)]) + str(aa[1*int(ii)]) + str(aa[2*int(ii)])
                                        + str(aa[3*int(ii)]) + str(aa[4*int(ii)]) + str(aa[5*int(ii)]) +
                                        str(aa[6*int(ii)])])
            else:
                if len(aa)>5:
                    spamwriter.writerow([str(b)] + [str(aa[0]) + str(aa[1]) + str(aa[2])
                                    + str(aa[3]) + str(aa[4]) + str(aa[5]) +
                                    str(aa[6])])

        print('----//----')
#    except:
#        print('Failed')

'''


