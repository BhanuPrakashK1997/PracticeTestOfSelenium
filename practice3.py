from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://itera-qa.azurewebsites.net/home/automation')
print(browser.title)

sel = Select(browser.find_element_by_xpath('//select[@class="custom-select"]'))
sel.select_by_visible_text("Norway")
time.sleep(2)

browser.close()
