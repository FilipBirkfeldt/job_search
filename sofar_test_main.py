# yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyes
# Main class for Filips Web-scraping tool :) 

# https://github.com/FilipBirkfeldt/job_search
# command+shift+P 


import time 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import numpy as np
import requests, bs4

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# upp till GITLAB 

print('\n')
print('---------------------------------------------START AV SCRIPTET------------------------------------------------------------------')
print('\n')

email = 'filip.birkfeldt@gmail.com'
password = ''
glassdoor = 'https://www.glassdoor.com/Job/sweden-data-science-jobs-SRCH_IL.0,6_IN223_KO7,19.htm'
linkedin = 'https://www.linkedin.com/jobs/search/?keywords=data%20scientist'
number_pages = 3

# Skapar driver-objekt samt beautiful.Soup - objekt 
driver=webdriver.Chrome('/Applications/chromedriver')
driver.get(glassdoor)
'''
source = urllib.request.urlopen(glassdoor)
soup = bs4.BeautifulSoup(source, 'html')
'''
# soup.select('div span')       hur en soup fungerar! 

# for-loopar så många sidor vi vill gå igenom 
'''
for i in range(1,number_pages):
    #Loopar igenom & hämtar info från page 1
    try: 
        next_button = driver.find_element_by_xpath('//*[@id="FooterPageNav"]/div/ul/li[7]/a')
    except: 
        break
    next_button.click() 
'''
job_vector=[]
for i in range(1, 31):
    # x_path = '//*[@id="MainCol"]/div[1]/ul/li[i]'
    i = str(i)
    x_path='//*[@id="MainCol"]/div[1]/ul/li['+(i)+(']')
    company_name = driver.find_element_by_xpath(x_path)
    job_info = company_name.text
    job_v1 = [job_info]
    job_v1 = job_v1[0].split('\n')
    job_vector.append(job_v1)

# Funktion som tar fram hur många kolumner som behövs i DataFrame: 
def col_nbr(lst):
    maxList = max(lst, key=lambda i:len(i))
    maxLength = len(maxList)
    return maxLength

#Antal kolumner som behövs: 
number_of_cols = col_nbr(job_vector)

def create_dataframe(list): 
    if number_of_cols == 5:
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    elif number_of_cols==6: 
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch', 'fill_out_1']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    elif number_of_cols==7: 
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch', 'fill_out_1', 'fill_out_2']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    else: 
        print('fel i create_dataframe... ')
    return df_jobb

df_jobb = create_dataframe(job_vector)
print(df_jobb)

#driver.find_element_by_xpath('//*[@id="FooterPageNav"]/div/ul/li[7]/a').click() 

#Stänger ner chrome
# driver.close()

