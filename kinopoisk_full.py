from selenium import webdriver
import requests
from itertools import cycle
import time
import csv
from kinopoisk.movie import Movie
from random import randint
import random
from selenium.common.exceptions import NoSuchElementException

#chromedriver_location = "/Users/sergeyone/Downloads/chromedriver"
#driver = webdriver.Chrome(chromedriver_location)
iwi = 0
with open("eais_movies_2015-2017_1.csv", "r") as input_file:
    csvreader = csv.reader(input_file, delimiter=",")
    for line in csvreader:
      #  try:
                movie_list = Movie.objects.search(str(line[0]))
                print(len(movie_list))
#            for i in range(0, len(movie_list) + 1):
                if len(movie_list) > 0:
                    d = movie_list[0].__dict__
                    print(d)
                    default_value = 1
                    print(d.get("id", default_value))
                    print(type(d.get("id", default_value)))
                    movie = Movie(id=d.get("id", default_value))
                    movie.get_content('main_page')
                    m = movie.__dict__
                    print(m)
                    with open('2019_kinopoisk_update_v0.1.csv', 'a', newline="") as csv_file:
                        writer = csv.writer(csv_file)
                        aaa = ''
                        for key, value in m.items():
                            aaa = aaa + ';' + str(value)
                        writer.writerow([str(line[0]) + '|' + aaa])
                        time.sleep(randint(5, 20))
                        iwi = iwi + 1
                        print('Done: ' + str(iwi) + ' movies')
        #except:
        #            print("Not found: " + str(iwi))
        #            iwi = iwi + 1
        #            time.sleep(randint(2, 11))

'''
        print(str(line[0]))
        movie_list = Movie.objects.search(str(line[0]))
        print(str(movie_list))
        d = movie_list[0].__dict__
        default_value = 1
        id = (d.get("id", default_value))
        print('as')


        driver.get('https://www.kinopoisk.ru/film/' + str(id) + '/')
        table_path = '//*[@id="infoTable"]/table/tbody'
        print(driver.find_element_by_xpath(table_path).text)
        time.sleep(randint(2, 11))

'''