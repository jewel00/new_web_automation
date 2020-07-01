#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2222.py
# @Time      :2020/6/27 15:56
# @Author    :江梅
from datetime import datetime
#计算时间差的分钟数
# 同一天的时间差

time_1 = '2020-03-02 15:00:00'
time_2 = '2020-03-02 16:00:00'

time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")
seconds = (time_2_struct - time_1_struct).seconds
print('同一天的秒数为：')
print(seconds)

# 不同天的时间差
time_1 = '2020-03-02 15:00:00'
time_2 = '2020-03-03 16:00:00'

time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")

# 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分，没有包含天数差，total_seconds包含天数差
# 所以total_seconds两种情况都是可以用的
total_seconds = (time_2_struct - time_1_struct).total_seconds()
print('不同天的秒数为：')
print(int(total_seconds))

min_sub = total_seconds / 60
print('不同天的分钟数为：')
print(int(min_sub))

if __name__ == "__main__":
    pass