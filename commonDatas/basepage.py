#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :basepage.py
# @Time      :2020/6/26 18:23
# @Author    :江梅
"""作为框架的基类来使用，把常用的操作封装在这里
    封装基本函数-执行日志、异常处理、失败截图
"""
from MyTools.get_my_log import Get_MyLog
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from MyTools.do_path import GetPath
import win32con
import win32gui
import time


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def wait_eleVisible(self,locator,doc='',times=10,poll_frequency=0.5):
        """
                :param locator: 元素定位，是元组类型，是loginLocators.py传过来的元素
                :param doc: 是描述从测试用例模块TestCases文件里面的测试用例传过来的，用于测试用例运行失败时截图名称使用，
                :param times: 等待时间，最大等待时间
                :param poll_frequency: 每几秒钟访问一次
                :return:
                """
        Get_MyLog().info("等待元素{0}可见".format(locator))
        try:
            #开始等待的时间
            #把时间转为字符串beforetime
            beforetime = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
            beforetime_struct = datetime.strptime(beforetime,"%Y-%m-%d %H:%M:%S")
            Get_MyLog().info("开始等待时间为：{}".format(beforetime_struct))
            WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            aftertime = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
            aftertime_struct = datetime.strptime(aftertime,"%Y-%m-%d %H:%M:%S")
            Get_MyLog().info("结束等待时间为：{}".format(aftertime_struct))
            # 求一个差值，写在日志的当中。等待了多久
            seconds = (aftertime_struct-beforetime_struct).seconds
            Get_MyLog().info("等待时长为:{}秒".format(seconds))
        except:
            # Get_MyLog().error("等待元素可见失败！,开始截图")
            self.save_Sreenshot(doc)
            raise

    #等待元素出现
    def wait_elePresence(self,locator,times=10,poll_frequency=0.5,doc=''):
        # Get_MyLog.info("等待{}元素出现".format(locator))
        #开始等待时间
        try:
            beforetime = datetime.now()
            beforetime_struct = datetime.strptime(beforetime,"%Y-%m-%d %H:%M:%S")
            Get_MyLog().info('开始等待时间为：{}'.format(beforetime_struct))
            WebDriverWait(self.driver,times,poll_frequency).until(EC.presence_of_element_located(locator))
            #结束等待时间
            aftertime = datetime.now()
            aftertime_struct = datetime.strptime(aftertime,"%Y-%m-%d %H:%M:%S")
            Get_MyLog().info('结束等待时间为：{}'.format(aftertime_struct))
            # 求一个差值，写在日志的当中。等待了多久
            seconds = (aftertime_struct - beforetime_struct).seconds
            Get_MyLog().info('等待的时间差为：{}S'.format(seconds))
        except:
            Get_MyLog().error('等待元素可见失败！,开始截图')
            self.save_Sreenshot(doc)
            raise

    #查找元素
    def get_element(self,locator,doc=''):
        Get_MyLog().info('查找元素：{}'.format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            Get_MyLog().error('查找元素失败！！！,开始截图')
            #截图
            self.save_Sreenshot(doc)
            raise
    #点击操作
    def click_element(self,locator,doc=""):
        #找元素
        ele = self.get_element(locator,doc)
        #元素操作
        Get_MyLog().info('{} 点击元素 {}'.format(doc,locator))
        try:
            ele.click()
        except:
            Get_MyLog().error("元素操作失败！！！,开始截图")
            #截图
            self.save_Sreenshot(doc)
            raise
    #输入元素
    def input_text(self,locator,text,doc=""):
        #找元素
        ele = self.get_element(locator,doc)
        #输入操作
        try:
            ele.send_keys(text)
        except:
            Get_MyLog().error("元素输入失败,开始截图")
            #截图
            self.save_Sreenshot(doc)
            #抛出异常
            raise

    #获取元素的文本内容
    def get_text(self,locator,doc=""):
        #找元素
        ele = self.get_element(locator,doc)
        try:
            return ele.text
        except:
            Get_MyLog().error("获取元素文本失败")
            #截图
            self.save_Sreenshot(doc)
            raise
    #获取元素的属性
    def get_element_arrtibut(self,locator,attribute_name,doc=""):
        """
        :param locator:
        :param attribute_name: 属性名称
        :param doc:
        :return:
        """
        ele = self.get_element(locator)
        try:
            return ele.get_attribute(attribute_name)
        except:
            Get_MyLog().error("获取元素属性失败！！！")
            # 截图
            self.save_Sreenshot(doc)
            raise

    #alter处理
    def alter_action(self,times=10,poll_frequency=0.5,action="accept",doc=''):
        """
        :param times:
        :param poll_frequency:
        :param action: 默认是接受，alter弹窗
        :param doc:
        :return:
        """
        # 等待alter出现
        try:
            WebDriverWait(self.driver,times,poll_frequency).until(EC.alert_is_present())
            # alert切换 不是html元素
            alert = self.driver.switch_to.alert
            if action == "accept":
                alert.accept()
            else:
                alert.dismiss()
        except:
            Get_MyLog().error("alter没有切换成功！！！")
            # 截图
            self.save_Sreenshot(doc)
            raise

    #iframe切换
    def switch_to_iframe(self,locator,iframe_reference,doc='',times=10,poll_frequency=0.5):
        """

        :param locator:
        :param iframe_reference: 被切换的iframe的元素定位名称
        :param doc:
        :param times:
        :param poll_frequency:
        :return:
        """
        #先切换到iframe，再查找元素
        try:
            WebDriverWait(self.driver,times,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(iframe_reference))
            self.get_element(locator,doc)
        except:
            Get_MyLog().error("iframe没有切换成功！！！")
            # 截图
            self.save_Sreenshot(doc)
            raise

    #上传操作
    def upload_file(self,file_path, browser_title):
        """

        :param file_path: 要打开文件的文件路径
        :param browser_title: 打开上传文件夹的窗口，左上角的浏览器旁边的文字
        :return:
        """

        dialog = win32gui.FindWindow("#32770", browser_title)  # 一级窗口
        comboboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级窗口
        combobox = win32gui.FindWindowEx(comboboxex32, 0, "ComboBox", None)  # 三级窗口
        edit = win32gui.FindWindowEx(combobox, 0, "Edit", None)  # 文本的输入窗口，第四级窗口
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")  # 二级窗口
        # 输入文件地址
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)  # 发送文件路径
        # 点击打开按钮 提交文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    # 截图操作，name是传进来的模块名或者函数名等，作为详细的路径
    def save_Sreenshot(self,doc):
        #图片名字：模块名_页面名称_操作名称_年-月-日_时分秒.png
        #截图存放的路径+操作名称+时间.png
        time = datetime.strftime(datetime.now(),"%Y-%m-%d_%H%M%S")
        file_name = GetPath.Screenshot_Path+doc+time+'.png'
        #给save_screenshot传递一个截图存放的文件名称
        self.driver.save_screenshot(file_name)
        Get_MyLog().info('截取网页成功。文件路径名称为：{}'.format(file_name))

    # 滚动条处理
    def scrollontoview(self):
        pass

    # 窗口切换
    def switch_to_windons(self):
        pass

if __name__ == "__main__":
    pass
