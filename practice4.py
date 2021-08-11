from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://itera-qa.azurewebsites.net/home/automation')
print(browser.title)

browser.find_element_by_xpath('//input[@type="radio"]/following-sibling::*[contains(.,"2")]').click()

time.sleep(2)

browser.find_element_by_xpath('//input[@id="selenium"]/following-sibling::*').click()
time.sleep(2)

browser.find_element_by_xpath('//input[@id="testng"]/following-sibling::*').click()
time.sleep(2)

browser.close()

