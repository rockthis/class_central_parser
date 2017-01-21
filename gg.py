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

driver = webdriver.Chrome('/Users/kostyafrolov/Downloads/chromedriver')


driver.get('https://www.class-central.com/subject/nutrition-and-wellness')

sleep(4)


# ua = UserAgent()
# header = {'user-agent': ua.chrome}
# page = requests.get('https://www.class-central.com/subject/nutrition-and-wellness', headers = header)
soup = BeautifulSoup(driver.page_source, 'lxml')
# # print(soup.prettify())
# # print(soup.find_all('tr', ))
course_name = []
for ana in soup.find_all('span', {'class' : 'course-name-text'}) :
    course_name.append(ana.text)
print(len(course_name))
# print(course_name[-1])
#
# # for temp in soup.find_all('span'):
# #   if temp.parent.name == 'a':
# #     print (temp.txt)
#
for el in soup.findAll('a' , { 'class' :  'course-name ad-name'}):
    print(el.findChildren('span')[0].text)
    course_name.append(el.findChildren('span')[0].text)
print(len(course_name))
#
# print(soup.find_all('a' , { 'class' :  'course-name ad-name'})[0].findChildren('span')[0].text)
# print(type(soup.findAll('a' , { 'class' :  'course-name ad-name'})))
#
# print(soup.findn)

driver.quit()


