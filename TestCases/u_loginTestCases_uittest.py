#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_testcases.py
# @Time      :2020/6/26 15:44
# @Author    :江梅
# from selenium import webdriver
# import unittest
# from PageObjects.loginPage import LoginPages
# from PageObjects.IndexPage import IndexPages
# from TestDatas.loginDatas import login_url,nornmal_Login_datas,unnormal_Login_datas01 as un01,unnormal_Login_datas02 as un02
# from ddt import ddt,data
#
#
#
#
# """登录页面元素操作（元素定位已经放在另外一个文件里面方便管理）"""
#
# @ddt
# class Login_TestCases(unittest.TestCase):
#     #setUpClass和tearDownClass对是一个类的前置数据和后置数据，
#     # setUp和tearDown是每一条测试用例的前置数据和后置数据
#     @classmethod
#     def setUpClass(cls):
#         #测试之前，开启和浏览器之间的会话
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(login_url)
#         cls.driver.maximize_window()
#
#     @classmethod
#     #当Login_TestCases所以的测试用例执行结束之后，关闭浏览器
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#     def tearDown(self):
#         #每一条测试完之后就刷新当前页面
#         self.driver.refresh()
#     # 正常登录用例
#     # 前置条件：在登录界面
#     # 操作步骤：输入账号、密码、是否选择记住手机号、点击登录
#     # 断言：是否跳转到首页(定位在首页的某个元素是否出现)
#
#     def test_3_normal_login_testcase(self):
#         LoginPages(self.driver).login(nornmal_Login_datas['usrname'],nornmal_Login_datas['passwd'],'正常登录模块_')
#         #这里是断言
#         self.assertTrue(IndexPages(self.driver).normallogin_Assertion())
#
#
#     #异常登录，当不输入账号/不输入手机号码/手机号码不再号码段内/手机号码不正确是，提示都是同一个类型
#     # 所以把同一类型的测试用例写在一起  通过ddt处理数据
#     @data(*un01)
#     def test_0_unnormal_login_testcases(self,logindata):
#         LoginPages(self.driver).login(logindata['usrname'],logindata['passwd'],'异常登录01函数_')
#         #断言
#         self.assertEqual(LoginPages(self.driver).unlogin_errMsg(),logindata['check'])
#
#     #异常登录，当电话手机没有授权时的提示是在中间弹出的
#     @data(*un02)
#     def test_1_unnormal_login_testcases(self, logindata):
#         LoginPages(self.driver).login(logindata['usrname'], logindata['passwd'],'异常登录02函数_')
#         #断言
#         self.assertEqual(LoginPages(self.driver).login_Popup_errMsg(), logindata['check'])
#
# if __name__ == "__main__":
#     pass