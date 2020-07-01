#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :do_path.py
# @Time      :2020/6/12 14:14
# @Author    :江梅
import os

class GetPath:
    Path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    Config_Path =os.path.join(Path,'test_config','config_file.config')
    Excel_Path = os.path.join(Path,'test_datas','test01.xlsx')
    Logging_Path = os.path.join(Path,'TestResults','logging_data.txt')
    TestHtml_Path = os.path.join(Path,'TestResults','test_result.html')
    Screenshot_Path = os.path.join(Path,'Outputs','screenshots_')


if __name__ == "__main__":
    print(GetPath.Screenshot_Path)
