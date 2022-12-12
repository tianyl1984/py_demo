#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' datetime demo '

from datetime import datetime, timedelta, timezone


def m1():
    now = datetime.now()
    print(now)
    date = datetime(2022, 12, 12, 15, 45, 0)
    print(date)
    print(date.timestamp())
    print(datetime.fromtimestamp(1670835100))
    print(datetime.utcfromtimestamp(1670835100))
    print(datetime.strptime('2022-12-12 15:50:40', '%Y-%m-%d %H:%M:%S'))
    print(now.strftime('%Y-%m-%d %H:%M'))
    # 时间直接加减操作
    print(now + timedelta(days=1))
    # 获取utc时间 带时区
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj)

m1()
