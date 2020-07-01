#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :IndexPage.py
# @Time      :2020/6/26 16:09
# @Author    :江梅
from PageLocators import loginLocators as LC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndexPages:

    def __init__(self,driver):
        self.driver = driver
    def normallogin_Assertion(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(LC.login_button_ele))
            return True
        except Exception as e:
            raise e
            return False

if __name__ == "__main__":
    IndexPages().normallogin_Assertion()