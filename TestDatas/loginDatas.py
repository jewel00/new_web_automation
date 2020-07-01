#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :loginDatas.py
# @Time      :2020/6/26 16:02
# @Author    :江梅
#登录页面
login_url = 'http://120.78.128.25:8765/Index/login.html'
#正常登录数据
nornmal_Login_datas = {"usrname":"18938837140","passwd":"python12"}

#异常登录数据: 不输入账号、不输入密码、账号过长，密码错误，电话号码不在号码段内
unnormal_Login_datas01= [{"usrname":"","passwd":"python12","check":"请输入手机号"},
                       {"usrname":"18938837140","passwd":"","check":"请输入密码"},
                       {"usrname":"1893883714099","passwd":"python12","check":"请输入正确的手机号"},
                       {"usrname":"11038837140","passwd":"python12","check":"请输入正确的手机号"}]

unnormal_Login_datas02 =[{"usrname":"18938837140","passwd":"python12","check":"此账号没有经过授权，请联系管理员!"}]

if __name__ == "__main__":
    pass