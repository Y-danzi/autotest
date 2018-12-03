# _*_ coding: utf-8 _*_
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir +'/tools/IEDriverServer.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'

    def __init__(self,driver):
        self.driver = driver


    #read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        #file_path = os.path.dirname(os.path.getcwd('.')) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        #config.read(file_path,encoding='utf-8'), 如果代码中有中文注释

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is: %s" %url)
        mobile_emulation = {'deviceName':'iPhone 6/7/8'}

        if browser == "Firefox":
            driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            #options = webdriver.ChromeOptions()
            #options.add_experimental_option('mobileEmulation',mobile_emulation)
            #driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)
            driver = webdriver.Ie(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")


        driver.get(url)
        logger.info("Open url: %s" %url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("Now, Close and quit the browser.")






