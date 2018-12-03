#coding = utf-8

import time
from selenium import webdriver
from test.basepage import BasePage


class BaiduSearch(object):

	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.implicitly_wait(10)

	basepage= BasePage(driver)

	def open_baidu(self):
		self.basepage.open_url("https://www.baidu.com")
		time.sleep(1)

	def test_search(self):
		self.driver.find_element_by_id('kw').send_keys("Selenium")
		time.sleep(1)
		self.driver.find_element_by_id('su').click()
		time.sleep(1)
		self.basepage.back()
		self.basepage.forward()
		self.basepage.quit_browser()

	def test_take_screen(self):
		self.basepage.take_screenshot()
		self.basepage.quit_browser()


baidu = BaiduSearch()
baidu.open_baidu()
#baidu.test_search()
baidu.test_take_screen()
