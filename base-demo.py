# -*- coding: utf-8 -*-
from collections.abc import Iterable


def print_demo():
    print('123')
    print('a', 'b', 'c')
    name = input('input your name: ')
    print('name:', name)


def str_demo():
    print('转义', '\\n')
    print('不转义', r'\n')
    str = '''
    第一行
    第二行
    '''
    print('多行字符串', str)
    # 格式化
    print('姓名：%s，年龄：%d' % ('张三', 14))
    print('姓名：{0}，年龄：{1}，成绩：{2:.1f}'.format('李四', 12, 10 / 3))
    name = '王五'
    score = 100 / 3
    print(f'姓名：{name}，成绩：{score:.2f}')

    # 取值
    print('ABCD'[2], 'ABCD'[-1])

    # 字符串是可迭代的
    print(isinstance('abc', Iterable))

    str = ' abc '
    print(str.strip())
    print(' ' in str)

def op_demo():
    print('10/3=', 10 / 3)
    print('10//3=', 10 // 3)


def bool_demo():
    flag = True
    print('flag:', flag)
    print('test:', 1 == -1)


def none_demo():
    test = None
    print('test:', test)
    if (not test):
        print('test is not true')


def if_demo():
    if (1):
        print(1)
    age = 10
    if (age < 10):
        print('<10')
    elif (age < 20):
        print('<20')
    else:
        print('>= 20')


def list_demo():
    list1 = ['a', 'b', 'c']
    list1.append('d')
    list1.insert(0, 'A')
    print(list1)
    print('pop:', list1.pop(), list1)
    # 切片 ::2 每2个取一个
    print(list1[0:2], list1[:2], list1[-2:], list1[::2], 'ABCDEFGHIJKLMN'[::3])
    # 循环获取下标
    for idx, val in enumerate(['a', 'b', 'c']):
        print(idx, val)


def tuple_demo():
    # tuple 不能修改
    tup = ('A', 'B', 'C')
    print(tup)
    print(('A',), ('A'))


def dict_demo():
    # key必须是不可变对象
    d = {'zhangsan': 10, 'lisi': 15}
    d['wangwu'] = 20
    print(d)
    print(d.get('wangwu'), 'wangwu' in d)
    print(d.get('wangwu1', 99))
    # 迭代
    for key in d:
        print(key, d[key])
    for val in d.values():
        print(val)
    for key, val in d.items():
        print(key, '=', val)


def set_demo():
    s = set([1, 2, 3])
    s.add(4)
    s.remove(2)
    # 不存在报错
    # s.remove(-1)
    print(s)


def type_covert():
    a = '123'
    print('转为数字:', int(a))
    # 判断类型
    print(isinstance(1, (int, float)))


def for_demo():
    print('range:', list(range(5)))
    for a in range(3):
        print(a)
    sum = 0
    num = 10
    while num > 0:
        if (num == 5):
            num = num - 1
            continue
        sum += num
        num = num - 1
    print(sum)


def list_creator():
    # 列表生成式
    # [exp for iter_var in iterable]
    print([x for x in range(5)])
    print([x * 2 for x in range(5)])
    print([x * 2 for x in range(5) if x > 0])
    # 双层
    print([x+y for x in 'ABC' for y in 'abc'])
    # 多变量
    print([key + '=' + str(val) for key,
          val in {'zhangsan': 12, 'lisi': 23}.items()])

def gen_demo1(num):
    while num > 0:
        print('gen_demo1', num)
        # generator函数，每next一次，执行到yield暂停
        yield num * num
        num = num - 1

def list_generator():
    # 列表生成器 生成器使用时才执行生成操作
    g = (x * x for x in range(10))
    print(g)
    # 每next一次，获取一个值
    # print(next(g), next(g))
    for num in g:
        print(num)
    print('generator函数')
    g2 = gen_demo1(3)
    for num in g2:
        print(num)

# list_generator()

str_demo()
