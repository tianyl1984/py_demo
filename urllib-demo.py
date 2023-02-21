#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' urllib demo '

from urllib import request
import json

def get_demo():
    req = request.Request('http://httpbin.org/get?a=1&b=2')
    req.add_header("accept", "application/json")
    with request.urlopen(req) as f:
        data = f.read()
        print('status:', f.status, f.reason)
        print('-------------------------------------')
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('-------------------------------------')
        result = data.decode('utf-8')
        print('Data:\n', result)
        obj = json.loads(result)
        print(obj['origin'])

get_demo()
