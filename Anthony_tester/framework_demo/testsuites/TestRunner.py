# _*_ coding: utf-8 _*_
import unittest
import os
import HTMLTestRunner
import time
import framework_demo.testsuites
from framework_demo.testsuites.test_baidu_search import BaiduSearch
from framework_demo.testsuites.test_get_page_title import GetPageTitle

report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

HtmlFile = report_path + now + 'HTMLtemplate.html'
fp = open(HtmlFile, 'wb')

#addTest方法，适用于用例少的时候
suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_search2'))
suite.addTest(GetPageTitle('test_get_title'))

#makeSuite方法，适用于一个类中用例多的时候
#suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
#suite1 = unittest.TestSuite(unittest.makeSuite(GetPageTitle))

#discover方法，适用于一个包下面多个类的时候
#suite = unittest.TestLoader().discover("testsuites")

if __name__=='__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="某某项目测试报告", description="用例测试情况")
    #runner = unittest.TextTestRunner()
    runner.run(suite)
    #runner.run(suite1)