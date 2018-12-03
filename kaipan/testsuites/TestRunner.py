# _*_ coding: utf-8 _*_
import unittest
import os
import HTMLTestRunner
import time
import testsuites
from testsuites.test_login import Login_in
from testsuites.test_kaipan_order import Order

report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

HtmlFile = report_path + now + 'HTMLtemplate.html'
fp = open(HtmlFile, 'wb')

#addTest方法，适用于用例少的时候
suite = unittest.TestSuite()
suite.addTest(Login_in('test_login_in'))
suite.addTest(Order('test_order'))



if __name__=='__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="某某项目测试报告", description="用例测试情况")
    runner.run(suite)
