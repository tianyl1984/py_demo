#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' urllib demo '

from urllib import request


def get_demo():
    req = request.Request('http://baidu.com')
    req.add_header("header1", "val")
    with request.urlopen(req) as f:
        data = f.read()
        print('status:', f.status, f.reason)
        print('-------------------------------------')
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('-------------------------------------')
        print('Data:\n', data.decode('utf-8'))

get_demo()
