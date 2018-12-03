# _*_ coding: utf-8 _*_
import time
import unittest
from framework_demo.framework.browser_engine import BrowserEngine
from framework_demo.pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()


    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """

        #封装基类和实现POM
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        homepage.sleep(2)
        homepage.get_windows_img()
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        homepage.sleep(2)
        homepage.get_windows_img()



if __name__ == '__mian__':
    unittest.main()
