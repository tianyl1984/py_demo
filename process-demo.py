#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' process demo '

from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def m1():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

if __name__=='__main__':
    m1()
