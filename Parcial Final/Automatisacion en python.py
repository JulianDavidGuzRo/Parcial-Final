import unittest
from selenium.webdriver.common.keys import Keys
from selenium  import webdriver

import time

chrome_driver = webdriver.Chrome("chromedriver.exe")
chrome_driver.get("https://www.instagram.com")

correo = chrome_driver.find_element_by_name("username")
correo.send_keys("guzmanjulian13@gmail.com")
correo.send_keys("Yvargas@uniempresarial.edu.co")

correo = chrome_driver.find_element_by_name("password")
correo.send_keys("cualquiera")

time.sleep(3)

correo.send_keys(Keys.ENTER)

time.sleep(3)

driver = chrome_driver

driver.excute_script("window.open(´´);")

time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.sonarqube.org")

driver.excute_script("window.open(´´);")
time.sleep(3)

driver.switch_to.window(driver.window_handles[2])
driver.get("https://id.cisco.com/")

driver.excute_script("window.open(´´);")
time.sleep(3)

driver.close()


