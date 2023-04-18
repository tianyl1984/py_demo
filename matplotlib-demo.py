#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' matplotlib demo '

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


def m1():
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


def m2():
    x = np.arange(0, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x, y1, label='sin')
    plt.plot(x, y2, linestyle='--', label='cos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('sin & cos')
    plt.legend()
    plt.show()


def m3():
    img = imread('C:\\Users\\tianyale\\Downloads\\2.png')
    plt.imshow(img)
    plt.show()

# m1()

# m2()


m3()
