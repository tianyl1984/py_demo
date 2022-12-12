#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' thread demo '

import time
import threading


def thread_run():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(3)
    print('thread %s ended.' % threading.current_thread().name)


def m1():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=thread_run, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


balance = 10


def change_balance(n):
    global balance
    balance = balance + n
    time.sleep(0.1)
    balance = balance - n


def thread_run_cb(n):
    for i in range(10):
        change_balance(n)


lock = threading.Lock()


def thread_run_cb_lock(n):  # 带锁的实现
    for i in range(5):
        lock.acquire()
        try:
            change_balance(n)
        finally:
            lock.release()


def thread_lock_demo():
    t1 = threading.Thread(target=thread_run_cb_lock, args=(5,))
    t2 = threading.Thread(target=thread_run_cb_lock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

# m1()


thread_lock_demo()
