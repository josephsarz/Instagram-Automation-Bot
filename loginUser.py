from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By
import accountInfoGenerator as account

def loginUser():
    browser= webdriver.Chrome("/usr/local/bin/chromedriver")
    browser.get("https://www.instagram.com/accounts/login/")
    time.sleep(10) #time.sleep count can be changed depending on the Internet speed.
    

    username = 'your username'
    password = 'your  password'

    #Fill the email value
    email_field = browser.find_element_by_name('username')
    email_field.send_keys(username)
    print('email : '+username)

    #Fill password value
    password_field  = browser.find_element_by_name('password')
    password_field.send_keys(password) #You can determine another password here.
    print('password : '+password)

    submit = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    submit.click()
    time.sleep(8)
    print('Login....')
