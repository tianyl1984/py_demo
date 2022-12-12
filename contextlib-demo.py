#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' contextlib demo '

from contextlib import contextmanager


class Insert(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('start')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('error')
        else:
            print('end')

    def execute(self):
        print('execute:%s' % self.name)


class Insert2(object):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print('execute:%s' % self.name)


def m1():
    # 通过自定义方法支持 with
    with Insert('zhangsan') as i:
        i.execute()


@contextmanager
def execute_cm(name):
    print('begin')
    i = Insert2(name)
    yield i
    print('end')


def m2():
    # 通过@contextmanager执行
    with execute_cm('zhangsan') as i:
        i.execute()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


def m3():
    with tag("h1"):
        print("hello")
        print("world")


# m1()
# m2()
m3()

