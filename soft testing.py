from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()

browser.get("http://localhost/amazonclone/") 

username = browser.find_element_by_id("/html/body/div[1]/div/ul[2]/li[2]/ul/div/div/div[2]/input[1]")
password = browser.find_element_by_id("/html/body/div[1]/div/ul[2]/li[2]/ul/div/div/div[2]/input[2]")
username.send_keys("navdeepkaur6359@gmail.com")
password.send_keys("12345678")
login_attempt = browser.find_element_by_xpath("/html/body/div[1]/div/ul[2]/li[2]/ul/div/div/div[2]/input[3]")
login_attempt.submit()
time.sleep(100)
element = browser.find_element_by_tag_name('h1')
if element.text == 'Welcome!':
    print("Pass")
else:
    print("Fail")