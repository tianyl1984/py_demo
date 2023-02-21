#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' json demo '

import json
from io import StringIO


class Student(object):
    def __init__(self, name):
        self.name = name


# 转换json方法
def toDict(stu):
    return {
        'name': stu.name
    }


def fromDict(stu):
    return Student(stu.get('name'))


def m1():
    d = dict(name='张三', age=12)
    # 序列化json
    print(json.dumps(d))
    f = StringIO()
    json.dump(d, f)
    json_str = f.getvalue()
    # 反序列化json
    print(json.loads(json_str))

    stu = Student('lisi')
    print(json.dumps(stu, default=toDict))
    # 通过lambda序列化
    print(json.dumps(stu, default=lambda obj: obj.__dict__))

    json_str = json.dumps(stu, default=toDict)
    print(json.loads(json_str, object_hook=fromDict))

def m2():
    json_str = '{"name":"aaa","age":3,"addressList":[{"city":"bj"},{"city":"sh"}],"names":[]}'
    user = json.loads(json_str)
    print(user)
    print(user["name"])
    print(user["addressList"][0]["city"])
    print(len(user["names"]))

# m1()
m2()
