#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2020/6/28 9:53
# @Author    :江梅
import pytest
from selenium import webdriver
from TestDatas.loginDatas import login_url
from PageObjects.loginPage import LoginPages
from MyTools.get_my_log import Get_MyLog

driver = None
#声明它是一个fixture scope="class"作用域为class： 类
#yield的前面是前置操作，后面是后置操作
@pytest.fixture(scope="class")
def access_web():
    Get_MyLog().info('进入测试......')
    #测试之前，开启和浏览器之间的会话
    #前置
    global driver
    driver = webdriver.Chrome()
    driver.get(login_url)
    driver.maximize_window()
    lg = LoginPages(driver)
    yield(driver,lg) #是分割线，后面可以接收返回值
    #后置
    driver.quit()
    Get_MyLog().info('测试结束！！！')

#声明它是一个fixture scope="funticon"（默认是函数）作用域为funticon：函数
@pytest.fixture()
def refresh_windons():
    global driver
    #不需要前置所以在yield前面不需要写
    yield
    #后置
    driver.refresh()


#1.单个标签
#在conftest.py添加如下代码，直接拷贝过去，把标签名改成你自己的就行了
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke"  # login_success 是标签名
    )


#2.多个标签
#在conftest.py添加如下代码，直接拷贝过去，把标签名改成你自己的就行了
# def pytest_configure(config):
#     marker_list = ["testmark1", "testmark2", "testmark3"]  # 标签名集合
#     for markers in marker_list:
#         config.addinivalue_line(
#             "markers", markers
#         )
if __name__ == "__main__":
    pass