#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' collections demo '

from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter


def namedtuple_demo():
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p)


def deque_demo():
    # deque 适合用于队列和栈,快速添加、删除
    q = deque(['a', 'b', 'c'])
    q.appendleft('0')
    print(q)


def defaultdict_demo():
    dd = defaultdict(lambda: None)
    dd['k1'] = 'a'
    # dict 不存在时报错，defaultdict 可以设置默认值
    print(dd['k1'], dd['k2'])


def ordered_dict_demo():
    # key有顺序 按插入顺序
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    od['0'] = 4
    print(od)


def chain_map_demo():
    d1 = {'key1': 11, 'key2': 12}
    d2 = {'key1': 21}
    # ChainMap 组合多个dict，按顺序查找其值
    cm = ChainMap(d2, d1, defaultdict(lambda: None))
    print(cm['key1'], cm['key2'], cm['key3'])


def counter_demo():
    c = Counter()
    for ch in 'hello':
        c[ch] = c[ch] + 1
    print(c)
    c.update('world')
    print(c)

# namedtuple_demo()
# deque_demo()
# defaultdict_demo()
# ordered_dict_demo()
#chain_map_demo()

counter_demo()