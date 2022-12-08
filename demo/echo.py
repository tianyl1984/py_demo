#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' echo demo '


def echo_exec(s):
    print(s)
    return s

# 区分直接执行还是导入，导入时 __name__ 不是 __main__
if __name__ == '__main__':
    echo_exec()
