from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By
import accountInfoGenerator as account

def createAccount():
    browser= webdriver.Chrome("/usr/local/bin/chromedriver")
    browser.get("http://www.instagram.com")
    time.sleep(10) #time.sleep count can be changed depending on the Internet speed.
    

    email = account.generatingEmail()
    username = account.username()
    fullname = account.generatingName()
    password = 'aa12345bb12345cc'+username

    #Save to File
    f=open("user_details.txt", "a+")
    f.write("email "+ email+"\n")
    f.write("username "+ username+"\n")
    f.write("fullname "+ fullname+"\n")
    f.write("password "+ password+"\n")
    f.close

    #Fill the email value
    email_field = browser.find_element_by_name('emailOrPhone')
    email_field.send_keys(email)
    print('email : '+email)

    #Fill the fullname value
    fullname_field = browser.find_element_by_name('fullName')
    fullname_field.send_keys(fullname)
    print('account : '+fullname)

    #Fill username value
    username_field = browser.find_element_by_name('username')
    username_field.send_keys(username)
    print('username : '+username)

    #Fill password value
    password_field  = browser.find_element_by_name('password')
    password_field.send_keys(password) #You can determine another password here.
    print('password : '+password)

    submit = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div[1]/button')
    submit.click()
    time.sleep(8)
    print('Registering....')
