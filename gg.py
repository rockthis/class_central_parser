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

sleep(5)



#       !!!     round-add-btn round-add-btn--plus
# ua = UserAgent()
# header = {'user-agent': ua.chrome}
# page = requests.get('https://www.class-central.com/subject/nutrition-and-wellness', headers = header)
soup = BeautifulSoup(driver.page_source, 'lxml')
# # print(soup.prettify())
# # print(soup.find_all('tr', ))
course_name = []
for ana in soup.find_all('span', {'class' : 'course-name-text'}) :
    course_name.append(ana.text)


quantify = soup.find_all('tr' , {'itemtype' : 'http://schema.org/Event' })

# itemtype="http://schema.org/Event

# print('quantify of companies:', quantify)

# for el in quantify:
#     path1 = el.findAll('a' , { 'class' :  'course-name ad-name'})

# print(course_name[-1])
#
# # for temp in soup.find_all('span'):
# #   if temp.parent.name == 'a':
# #     print (temp.txt)
#
for el in soup.findAll('a' , { 'class' :  'course-name ad-name'}):
    print(el.findChildren('span')[0].text)
    course_name.append(el.findChildren('span')[0].text)
print('with ads:' , len(course_name))
for el in course_name:
    print(el)

search_bar = driver.find_element_by_xpath('//*[@id="course-listing-tbody"]/tr[2]/td[4]')
print(search_bar.get_attribute('data-timestamp')[0:3])

print(driver.find_element_by_xpath('//*[@itemtype="http://schema.org/Event"]').get_attribute('itemtype'), '!!!!')

company_names = []

company_names = driver.find_elements_by_xpath('//*[@itemtype="http://schema.org/Event"]/td[2]/a/span')

print(len(company_names))

print(company_names[0].text)

# company_names = []
#
# for el in temp:
#     company_names.append(el.text)
#
# print(len(company_names))
# //*[@id="course-listing-tbody"]/tr[2]/td[2]/a/span
# print(soup.find_all('a' , { 'class' :  'course-name ad-name'})[0].findChildren('span')[0].text)
# print(type(soup.findAll('a' , { 'class' :  'course-name ad-name'})))
#
# print(soup.findn)

driver.quit()


