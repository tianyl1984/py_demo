#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' oop demo '


class Student(object):
    # __slots__ 可以执行只允许存在的属性
    # __slots__ = ('name', 'age')
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # len() 会执行此方法
    def __len__(self):
        return self.score

    # print打印使用
    def __str__(self):
        return self.name + ':' + str(self.score)

    def print_score(self):
        print('name:%s,score:%d' % (self.name, self.score))

# 各种特殊变量和函数 https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904

class Teacher(object):

    # name的get方法
    @property
    def name(self):
        # 不能使用name，name是方法名，导致循环调用
        return self._name

    # name的set方法
    @name.setter
    def name(self, val):
        self._name = val


def stu_demo():
    zs = Student('zhangsan', 78)
    zs.print_score()
    # 获得一个对象的所有属性和方法
    print(dir(zs))
    print(len(zs))
    print(zs)


def teacher_demo():
    t = Teacher()
    t.name = 'aaa'
    print(t.name)


stu_demo()

# teacher_demo()
