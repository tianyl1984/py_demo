#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' numpy demo '

import numpy as np


def m1():
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([2.0, 4.0, 6.0])
    print(x)
    print(y)
    print(x + y)
    print(x - y)
    print(x * 2)
    print(x * y)
    print(x / y)
    print('--------------------')
    a = np.array([[1, 2], [3, 4], [5, 6]])
    b = np.array([[7, 8], [9, 10], [11, 12]])
    print(a + b)
    print(a[1][1])
    print(b.flatten())
    print('--------------------')
    print(b.flatten()[np.array([1, 3, 5])]) # 索引为 1,3,5 的元素
    c = b.flatten()
    print(c[c > 10]) # 筛选大于10的值


m1()
