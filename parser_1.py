import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')

def news_parser():
    rq = requests.get('https://habr.com/ru/flows/popsci/articles/')
    srq = BeautifulSoup(rq.content, "html.parser")

    links = srq.find_all("h2")
    count = 5
    result_links = []

    for link in links: 
        a_tag = link.find('a') 

        if a_tag and count != 0:  
            result_links.append(a_tag.get('href'))  
            count -= 1  

    return result_links 
                
def bus_parser():
    pass

def elec_parser(from_point, to_point):
    url = 'https://www.tutu.ru/'
    
    driver = webdriver.Chrome()
    driver.get(url)

    driver.implicitly_wait(2)

    driver.find_element(By.CSS_SELECTOR, 'tab t-ttl_third tab_etrain j-tab').click()

    driver.find_element(By.CSS_SELECTOR, 'input_field j-station_input  j-station_input_from')
    element.send_keys(from_point)

    driver.find_element(By.CSS_SELECTOR, 'input_field j-station_input  j-station_input_to')
    element.send_keys(to_point)

    driver.find_element(By.CSS_SELECTOR, 'input_field j-permanent_open j-input j-date_to').click()

    driver.find_element(By.CSS_SELECTOR, 'ui-datepicker-current ui-state-default ui-priority-secondary ui-corner-all').click()

    driver.find_element(By.CSS_SELECTOR, 'spinner').click()

    element = driver.find_element(By.CLASS_NAME, 'desktop__card__yoy03')
    
    print(element)

    driver.close()

elec_parser('Кубинка', 'Москва Белорусская')