from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('http://www.yahoo.com/')

assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p') # Q is the browser search element name
elem.send_keys('How many potatoes are in Ireland?' + Keys.RETURN)

sleep(5)

browser.quit()