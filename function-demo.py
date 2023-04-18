# -*- coding: utf-8 -*-

import functools

def m1():
    print('m1')


def empty():
    # 空函数 占位
    pass


def m2():
    # 多值返回
    return 1, 2


def m3(x):
    # 位置参数
    return 2 * x


def m4(x, y=3):
    # y默认值为3，可不传 默认参数必须指向不变对象！ 函数在定义时初始化默认值，如果为不可变对象，就会'记住'此值
    return x * y


def m5(*nums):
    # 可变长参数 把参数转为list传入
    sum = 0
    for num in nums:
        sum = sum + num
    return sum


def m6(**kw):
    # 关键字参数 把参数转为dict传入
    for key in kw:
        print(key, kw[key])


def m7(*, name, age=0):
    # 命名关键字 按命名传入，不用考虑顺序，不传的参数需要有默认值  当存在可变参数时不需要'*,'，比如: def m7(a, *nums, name, age):
    print(name)
    print(age)


def m8(a, b=1, *nums, name, age, **kw):
    print(a, b, nums, name, age, kw)


def m9():
    # 创建偏函数，生成一个新函数
    int2 = functools.partial(int, base=2)
    print(int2('1011'))

m1()
empty()
print(m2())
print('位置参数:', m3(5))
print('默认值参数:', m4(5))
print('可变长参数:', m5(1, 2), m5(1, 2, 3))
print('关键字参数:', m6(name='zhangsan', age=12))
print('命名关键字:', m7(name='lisi', age=14), m7(
    name='wangwu'), m7(age=6, name='xiaoliu'))
print(m8('张三', 20, 1, 2, name='lisi', age=5, birth=1988))
print(m1.__name__)
m9()
