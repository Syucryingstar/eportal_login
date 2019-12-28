# -*- coding: utf-8 -*-
# @Time : 2019/12/14 18:45
# @Author : Syu
from urllib import parse
import requests


def login(username, password):
    """
    eportal登录
    :param username: 账号
    :param password: 密码
    :return: 
    """
    response_get_url = requests.get("http://2.2.2.2")  # 获取登录url信息
    # print(response_get_url.text)
    referer = response_get_url.text.split("'")[1]
    # print(referer)
    query_string = parse.quote(referer.split("?")[1], encoding='utf-8')
    print("query_string: " + query_string)
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6'
                      '1.0.3163.91 Safari/537.36',
        'Referer': referer
    }
    
    data = {
        "userId": username,
        "password": password,
        "queryString": query_string,
        "passwordEncrypt": 'false',
        "service": "",
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": ""
    }
    url_login = 'http://192.168.112.224/eportal/InterFace.do?method=login'

    response_login = requests.post(url_login, headers=headers, data=data)  # 登录

    result = eval(response_login.content.decode('utf-8').replace('null', '"null"'))
    if 'success' in result['result']:
        print("登录成功！")
    else:
        print(result['message'])
        print("登录失败！")


if __name__ == '__main__':
    un = ""
    pw = ""
    login(un, pw)
