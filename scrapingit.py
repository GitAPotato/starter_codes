"""
	requires selenium install
"""

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://isslive.com/displays/adcoDisplay1.html')
# time to load webpage and allow isslive.com to fulfill position request
time.sleep(3)

# USLAB000032 is id for xPos
for i in range(0, 5):
    print('@ ' + str(driver.find_element_by_id('USLAB000102').text))
    print('xPos: ' + str(driver.find_element_by_id('USLAB000032').text))
    print('yPos: ' + str(driver.find_element_by_id('USLAB000033').text))
    print('zPos: ' + str(driver.find_element_by_id('USLAB000034').text))
    print('xVel: ' + str(driver.find_element_by_id('USLAB000035').text))
    print('yVel: ' + str(driver.find_element_by_id('USLAB000036').text))
    print('zVel: ' + str(driver.find_element_by_id('USLAB000037').text))
    time.sleep(5)
driver.close()
