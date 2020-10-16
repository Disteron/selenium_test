import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROJECT_ROOT = os.path.dirname(__file__)

CHROME_DRIVER = os.path.join(PROJECT_ROOT, 'webDriverChrome/chromedriver')

def trading():
    set=Options()
    set.add_argument("--window-size=1920,1080")
    driver=webdriver.Chrome(executable_path=CHROME_DRIVER, options=set)
    driver.get("https://tradingmeetup2021.com/")
    sleep(2)
    driver.find_element_by_xpath('//label[@for="radio_2"]').click()
    driver.find_element_by_xpath('//input[@class="sg_email"]').send_keys('test@mail.ru')
    driver.find_element_by_xpath('//input[@class="sg-submit-btn btn bounceIn"]').click()
    driver.quit()

trading()