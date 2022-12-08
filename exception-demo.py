#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' built in function demo '

import logging


def m1(numStr):
    print('exe m1 method')
    try:
        print('in try')
        r = 10 / int(numStr)
    except ValueError as e:
        print('ValueError:', e)
        logging.exception(e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
        logging.exception(e)
    else:
        print('no error')
    finally:
        print('in finally')
    print('end')


class CustomError(BaseException):
    # 自定义异常
    pass


def m2(num):
    if (num == 0):
        raise CustomError('num 不能为 0')
    print(10/num)

# m1('0')


m2(0)
