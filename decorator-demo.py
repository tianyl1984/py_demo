#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' decorator demo '

def log(fun):
    def wrapper(*args, **kw):
        print('before', fun.__name__)
        return fun(*args, **kw)
        # print('after', fun.__name__)
    return wrapper

def log2(name):
    def decorator(fun):
        def wrapper(*args, **kw):
            print(name, 'before', fun.__name__)
            return fun(*args, **kw)
        return wrapper
    return decorator

# @log
@log2('time-log')
def time():
    return '2022-12-08'

print(time())