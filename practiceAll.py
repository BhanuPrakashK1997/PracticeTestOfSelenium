from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://itera-qa.azurewebsites.net/home/automation')
print(browser.title)
#xpaths in practice test 1
enter_name_xpath = '//input[@id="name"]'
mobile_no_xpath = '//input[@id="phone"]'
email_xapth ='//input[@id="email"]'
password_xpath ='//input[@id="password"]'
address_xpath = '//textarea[@id="address"]'
submit_xpath = '//button[@name="submit"]'

#xpaths in prcatice test2
gender_xpath = '//input[@id="male"]'
weekday_xpath = '//input[@id="tuesday"]'
weekday2_xpath = '//input[@id="friday"]'


#browser send operation practice 1
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

#browser send operations prcatice 2

browser.find_element_by_id('male').click()
time.sleep(2)
browser.find_element_by_id('tuesday').click()
time.sleep(2)
browser.find_element_by_id('friday').click()
time.sleep(2)



#practice 3 its is conatins of (Select module) on using select value from DropDown list
sel = Select(browser.find_element_by_xpath('//select[@class="custom-select"]'))
sel.select_by_visible_text("Norway")
time.sleep(2)



#practice 4 -- radio and check box click bye using xpath (included sibblings)

browser.find_element_by_xpath('//input[@type="radio"]/following-sibling::*[contains(.,"2")]').click()
time.sleep(2)
browser.find_element_by_xpath('//input[@id="selenium"]/following-sibling::*').click()
time.sleep(2)
browser.find_element_by_xpath('//input[@id="testng"]/following-sibling::*').click()
time.sleep(2)

browser.close()

