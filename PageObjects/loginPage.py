#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_Page.py
# @Time      :2020/6/26 15:14
# @Author    :江梅
from selenium import webdriver
from PageLocators import loginLocators as LC
from commonDatas.basepage import BasePage #导入封装好的元素操作类
#引入元素定位的文件

"""登录页面元素操作（元素定位已经放在另外一个文件里面方便管理）"""
#继承基本类
class LoginPages(BasePage):
    #已经继承基本类，基类有初始化函数，这里不需要

    #登录操作
    def login(self,usrname,passwd,doc='',login_remembe = True):
        #直接调用封装里面的函数
        self.wait_eleVisible(LC.login_usrname_ele,doc)
        self.input_text(LC.login_usrname_ele,usrname,doc)
        self.input_text(LC.login_password_ele,passwd,doc)
        # #是否需要记住账号，做了个判断，默认是勾选
        if login_remembe:
            pass
        else:
            self.click_element(LC.login_remembe_ele,doc)
        self.click_element(LC.login_button_ele,doc)

    #当异常登录时，在首页显示的错误信息封装在这里，利用这些错误信息来作为测试用例的断言，
    # 下面的是不同的两种错误类型
    #1、在输入框下的错误提示
    def unlogin_errMsg(self):
        self.wait_eleVisible(LC.unlogin_errMsg_ele)
        return self.get_text(LC.unlogin_errMsg_ele)

    #2、弹出来的错误提示
    def login_Popup_errMsg(self,doc=''):
        self.wait_eleVisible(LC.login_Popup_errMsg_ele,doc)
        return self.get_text(LC.login_Popup_errMsg_ele,doc)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('http://120.78.128.25:8765/Index/login.html')
    driver.maximize_window()
    LoginPages().login("18938837140","python12")