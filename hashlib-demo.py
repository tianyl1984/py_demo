#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' hashlib demo '

import hashlib

def md5():
    s = '123456'
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    print(md5.hexdigest())


md5()
