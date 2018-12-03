# _*_ coding: utf-8 _*_
from framework_demo.framework.base_page import BasePage

class SportNewsHomePage(BasePage):
    nba_link = "xpath=>//*[@id='col_nba']/div/div[2]/ul[1]/li[1]/a"

    def click_nab_link(self):
        self.click(self.nba_link)
        self.sleep(2)