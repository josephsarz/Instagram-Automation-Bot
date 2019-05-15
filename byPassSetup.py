from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def byPassSetup():
    follow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div/div[1]/div/div/div[2]/div[3]/button')
    follow.click()
    time.sleep(8)
    print('following....')
