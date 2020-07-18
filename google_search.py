from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get("https://www.google.com/")
assert "Google" in browser.title

search_bar = browser.find_element_by_name('q')
search_bar.send_keys("How many potatoes are in Ireland"+ Keys.RETURN)

sleep(5)

browser.quit()