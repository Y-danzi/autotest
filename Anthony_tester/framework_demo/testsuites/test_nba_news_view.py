# _*_ coding: utf-8 _*_
import time
import unittest
from framework_demo.framework.browser_engine import BrowserEngine
from framework_demo.pageobjects.baidu_homepage import HomePage
from framework_demo.pageobjects.baidu_news_home import NewsHomePage
from framework_demo.pageobjects.news_sport_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        baiduhome = HomePage(self.driver)
        baiduhome.click_news()

        newshome = NewsHomePage(self.driver)
        newshome.click_sports()

        sportnewhome = SportNewsHomePage(self.driver)
        sportnewhome.click_nab_link()
        sportnewhome.get_windows_img()

if __name__=='__main__':
    unittest.main()