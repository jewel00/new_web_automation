#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_testcases.py
# @Time      :2020/6/26 15:44
# @Author    :江梅


from PageObjects.IndexPage import IndexPages
from TestDatas.loginDatas import nornmal_Login_datas,unnormal_Login_datas01 as un01,unnormal_Login_datas02 as un02
import pytest
import time
"""登录页面元素操作（元素定位已经放在另外一个文件里面方便管理）"""
@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_windons")
class Test_LoginCases:
    # 异常登录，当不输入账号/不输入手机号码/手机号码不再号码段内/手机号码不正确是，提示都是同一个类型
    #@pytest.mark.parametrize("参数名",列表数据) 和ddt的用法差不多

    @pytest.mark.parametrize("logindata", un01)
    def test_unnormal_login(self, logindata,access_web):
        doc = '登录模块_异常登录01函数_'
        access_web[1].login(logindata['usrname'], logindata['passwd'],doc=doc)
        # 断言
        assert access_web[1].unlogin_errMsg(), logindata['check']

    # 异常登录，当电话手机没有授权时的提示是在中间弹出的
    @pytest.mark.parametrize("logindata", un02)
    def test_Popuperror_login(self, logindata,access_web):
        doc = '登录模块_异常登录02函数_'
        access_web[1].login(logindata['usrname'], logindata['passwd'],doc=doc)
        # 断言
        assert access_web[1].login_Popup_errMsg(), logindata['check']

    @pytest.mark.smoke
    def test_normal_login(self,access_web):
        doc = '登录模块_正常登录_'
        access_web[1].login(nornmal_Login_datas['usrname'],nornmal_Login_datas['passwd'],doc=doc)
        #这里是断言
        assert IndexPages(access_web[0]).normallogin_Assertion()




if __name__ == "__main__":
    pytest.main(["-s", "test_loginTestCases_pytest.py"])