#coding=utf-8
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.souhu.com')
time.sleep(1)

try:
	assert "百度一下" in driver.title
	print("Assertion test pass.")
except Exception as e:
	print("Assertion test fails.",format(e))

print(driver.title)