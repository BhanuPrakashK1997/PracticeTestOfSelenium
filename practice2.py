from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://itera-qa.azurewebsites.net/home/automation')
print(browser.title)

gender_xpath = '//input[@id="male"]'
weekday_xpath = '//input[@id="tuesday"]'
weekday2_xpath = '//input[@id="friday"]'

browser.find_element_by_id('male').click()
time.sleep(2)
browser.find_element_by_id('tuesday').click()
time.sleep(2)
browser.find_element_by_id('friday').click()
time.sleep(2)

browser.close()
