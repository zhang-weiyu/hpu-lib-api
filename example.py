# -*- coding: utf-8 -*-
"""
@Author    : zhjue
@Date      : 2020-12-21
@Software  : VSCode
"""

# -*- coding: utf-8 -*-

import requests
from datetime import date, timedelta

headers = {
    'user-agent': 'Dart/2.5 (dart:io)',
    'host': 'seatlib.hpu.edu.cn:8443'
}


def getDate():
    return date.today() + timedelta(days=1)


def freeBook(token: str):
    res = requests.post(
        'http://seatlib.hpu.edu.cn/rest/v2/freeBook',
        headers=headers,
        data={
            'token': token,
            'seat': '',  # 此处填写要预约的座位ID，见(新图书馆座位编号.json)
            'startTime': '',  # 预约时间段的起始时间，按分钟计算，如10点为600
            'endTime': '',  # 预约时间段的结束时间，按分钟计算，如14点为840
            'date': getDate()
        })
    return res.json()


def main():
    url = 'http://seatlib.hpu.edu.cn/rest/auth'
    res = requests.get(
        url=url,
        headers=headers,
        params={
            'username': '',  # 此处填写学号
            'password': ''  # 此处填写图书馆密码
        })

    if res.status_code == 200:
        print('login success')
        print(res.text)
        res1 = res.json()
        print(res)
        token = res1['data']['token']
        info = freeBook(token)
        print(info)


if __name__ == "__main__":
    main()