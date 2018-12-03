# _*_ coding: utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.kaipan_order import OrderPage



class Order(unittest.TestCase):
    #def setUp(self):
        #browse = BrowserEngine(self)
        #self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_order(self):
        orderroom = OrderPage(self.driver)
        #orderroom.read_cookie()
        orderroom.click_room()
        orderroom.agree()
        orderroom.sub_roomdetail()
        orderroom.get_windows_img()

if __name__=='__main__':
    unittest.main()