#coding=utf-8
import time
from test.browser_engine import BrowserEngline


class TestBrowserEngine(object):

	def open_browser(self):
		browserengine = BrowserEngline(self)
		self.driver = browserengine.get_browser()
		time.sleep(1)

tbe = TestBrowserEngine()
tbe.open_browser()
	