from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://itera-qa.azurewebsites.net/home/automation')
print(browser.title)



enter_name_xpath = '//input[@id="name"]'
mobile_no_xpath = '//input[@id="phone"]'
email_xapth ='//input[@id="email"]'
password_xpath ='//input[@id="password"]'
address_xpath = '//textarea[@id="address"]'
submit_xpath = '//button[@name="submit"]'

browser.find_element_by_id('name').send_keys('Bhanu prakash')
time.sleep(2)
browser.find_element_by_id('phone').send_keys('9542461632')
time.sleep(2)
browser.find_element_by_id('email').send_keys('bhnnau@gmail.com')
time.sleep(2)
browser.find_element_by_id('password').send_keys('789456123')
time.sleep(2)
browser.find_element_by_id('address').send_keys('bangalore')
browser.find_element_by_name('submit').click()
time.sleep(2)

browser.close()