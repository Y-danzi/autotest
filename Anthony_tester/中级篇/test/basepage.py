# coding=utf-8
import os
import time
from test.logger import Logger

mylog = Logger(logger='BasePage').getlog()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def open_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def take_screenshot(self):
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        print(file_path)

        rq = time.strftime('%Y%m%d%H%M%S', time.localtime())
        screen_name = file_path + rq + '.png'
        print(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("开始截图并保存")

        except Exception as e:
            mylog.error("出现异常", format(e))
