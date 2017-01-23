import requests
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from xlsxwriter import Workbook
import xlrd
import re
import json
from openpyxl import load_workbook
from lxml import etree
from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome('/Users/kostyafrolov/Downloads/chromedriver')   mac

driver = webdriver.Chrome('C:\\Users\\Admin\\Downloads\\chromedriver')    #windows

driver.get('https://www.class-central.com/subject/nutrition-and-wellness')

sleep(5)

course_rate = []
course_name = []
course_provider = []

course_rates = driver.find_elements_by_xpath('//*[@itemtype="http://schema.org/Event"]/td[4]')

# print(search_bar.get_attribute('data-timestamp')[0:3])

course_names = driver.find_elements_by_xpath('//*[@itemtype="http://schema.org/Event"]/td[2]/a/span')

course_providers = driver.find_elements_by_xpath('//*[@itemtype="http://schema.org/Event"]')

print(len(course_providers))
# /td[2]/ul/li/a

provider1 = []
provider2 = []

for el in course_providers:
     len = el.find_elements_by_xpath('td[2]/ul/li[1]/a')    #!!!!!!! len нужно заменить
     if len:
        for temp in len:
            print(temp.text)
            provider1.append(temp.text)
     else:
        provider1.append('No provider')
     scndprovider = el.find_elements_by_xpath('td[2]/ul/li[2]/a')
     if scndprovider:
         for temp in scndprovider:
             print('2ndprovider', temp.text)
             provider2.append(temp.text)
             print(provider2.__len__())
     else:
         print('ss')





    # course_provider.append(el.text)

for el in course_rates:
    course_rate.append(el.get_attribute('data-timestamp')[0:3])

for el in course_names:
    course_name.append(el.text)

# print(len(course_name),len(course_provider),len(course_rate))

# for i in range(len(course_rate)):
#     print(course_name[i], '=' ,course_provider[i] , '=', course_rate[i])




driver.quit()


