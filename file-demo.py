#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' file demo '

from io import StringIO
from io import BytesIO

def m1():
    try:
        f = open('./a.txt', 'r', encoding='utf-8')
        print(f.read())
    finally:
        if f:
            f.close()


def m2():
    # r:只读  w:写  b:二进制  a:写文件时追加文件 
    with open('./a.txt', 'r', encoding='utf-8') as f:
        # 读取全部 read(size) 指定 最多读取size个字节
        print(f.read())


def m3():
    with open('./a.txt', 'r', encoding='utf-8') as f:
        # 读取所有行，返回list
        print(f.readlines())


def strio_demo():
    # 只写字符流
    f = StringIO()
    f.write('zhangsan\n')
    f.write('lisi')
    print(f.getvalue())

    # 只读字符流
    f = StringIO('a\nb\nc')
    # 按行读，结果包含换行符
    print(f.readlines())

def byteio_demo():
    f = BytesIO()
    f.write('呵呵'.encode('utf-8'))
    print(f.getvalue())

    f = BytesIO('哈'.encode('gbk'))
    print(f.read())

# m1()
# m2()
# m3()
# strio_demo()
byteio_demo()

