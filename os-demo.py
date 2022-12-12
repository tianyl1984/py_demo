#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' os module demo '

import os


def m1():
    print(os.name)
    # windows没有uname方法
    if (os.name != 'nt'):
        print(os.uname())
    print(os.environ)


def m2():
    print(os.path.abspath('.'))
    new_dir = os.path.join(os.path.abspath('.'), 'abc')
    if (not os.path.exists(new_dir)):
        # os.makedirs(new_dir) 创建多层
        print(os.mkdir(new_dir))
    # 删除文件夹
    print(os.rmdir(new_dir))
    # 列出目录
    print([x for x in os.listdir('.') if os.path.isdir(x)])


# m1()
m2()
