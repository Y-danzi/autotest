# coding=utf-8
 
from selenium import webdriver
 
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
 
driver.get("https://www.baidu.com")
try:
    driver.find_element_by_id("w")
    print ('test pass: ID found')  
except Exception as e:
    print ("Exception found", format(e))
 
driver.quit()
