# _*_ coding: utf-8 _*_
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.kaipan_loginpage import HomePage
from pageobjects.kaipan_order import OrderPage
class Login_in(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    #def tearDown(self):
     #   self.driver.quit()

    def test_login_in(self):
        homepage = HomePage(self.driver)
        homepage.click_login()
        homepage.input_username("测试")
        homepage.input_phone('13333333331')
        homepage.input_msgcode('1111')
        homepage.input_idcard('123456789012345678')
        homepage.click_login_button()
        homepage.click_confirm_button()
        homepage.get_windows_img()
        homepage.get_cookie()


        try:
            assert '欢迎您' in homepage.loginsucess()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))




if __name__=='__main__':
    unittest.main()