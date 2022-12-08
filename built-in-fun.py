#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' built in function demo '

from functools import reduce
import types

def m1(x):
    print(x)
    return x


def m2(x1, x2):
    print(x1, x2)
    return x1 + x2


def m3(x):
    return x % 2 == 0


def map_demo():
    r = map(m1, list(range(3)))
    # r为Iterator，惰性序列，获取其值时才执行m1
    print(list(r))


def reduce_demo():
    r = reduce(m2, list(range(4)))
    print('结果:', r)


def filter_demo():
    r = filter(m3, list(range(4)))
    print('结果:', list(r))
    # lambda 表达式
    print('结果2:', list(filter(lambda x: x % 2 == 0, list(range(10)))))


def sort_demo():
    print(sorted([36, 5, -12, 9, -21]))
    # 指定排序方法
    print(sorted([36, 5, -12, 9, -21], key=abs))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

def type_demo():
    print(type(sort_demo) == types.FunctionType)
    print(type(abs) == types.BuiltinMethodType)
    print(type(lambda x:x) == types.LambdaType)

# map_demo()
# reduce_demo()
# filter_demo()
# sort_demo()
type_demo()
