# _*_ coding: utf-8 _*_
from framework_demo.framework.base_page import BasePage

class NewsHomePage(BasePage):
    sports_link = "xpath=>//*[@id='channel-all']/div/ul/li[7]/a"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)