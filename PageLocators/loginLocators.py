#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :loginlocators.py
# @Time      :2020/6/26 14:59
# @Author    :江梅
from selenium.webdriver.common.by import By

"""这个文件专门存放元素定位数据，和元素操作分离"""

login_usrname_ele = (By.XPATH,'//*[@name="phone"]')
login_password_ele = (By.XPATH,'//*[@name="password"]')
login_remembe_ele = (By.XPATH,'//*[@name="remember_me"]')
login_button_ele = (By.XPATH,'//*[@class="btn btn-special"]')
login_register_ele = (By.XPATH,'//*[@href="/Index/reg.html"]')
unlogin_errMsg_ele = (By.XPATH,'//*[@class="form-error-info"]')
login_Popup_errMsg_ele = (By.XPATH,'//*[@class="layui-layer-content"]')


if __name__ == "__main__":
    pass