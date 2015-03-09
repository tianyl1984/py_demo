#coding:utf-8
import os
import time
import math
import sys

print u"hello,中文"

a = u"this is a demo 中文"
print a.upper()
print a.islower()
print len(a)
print a[:4]

def add_fun(a,b):
		c = a + b
		print u"和为：%d"%c
if __name__ == "__main__":
	add_fun(1,2)
print u"input a str"
#b=raw_input()
b=u"123"
print u"输入：%s"%b
c=int(b)
if c < 10:
	print "%d less 10"%c
else:
	print "%d bigger 10"%c

list1 = [1,"abc",True,"123"]
print list1
print len(list1)
list1.append(u"中文")
print list(reversed(list1))
#count统计出现次数
print list1.count(True)
list1.insert(10,"pos10")
list1.insert(9,"pos9")
print list1
if "abc" in list1:
	list1.remove("abc")
else:
	print u"abc not in list1"
print list1

#range 得到数字list

list2 = range(0,10,2)
print list2

list2.sort(reverse=True)
print list2

str1 = u"i am learning python"
print str1.split()

print "_".join(str1.split())

for a in str1.split():
	print a,
print ""
for i in range(len(str1.split())):
	print str1.split()[i] + ",",
print ""

list3 = [" apple","oriange "," green "]
print [one.strip() for one in list3]
for (i,name) in enumerate(list3):
	print str(i) + ":" + name

#字典
print u"字典"
dict1 = {"1":"one","2":"two","3":"three"}
dict1["4"] = "four"
print dict1
print dict1.keys()
print dict1.values()
print dict1.items()

#元组
print u"元组"
t1 = 1,2,"abc","def"
print t1
print t1[1:2]
print list(t1) #tuple-->list
print tuple(list3) #list-->tuple
for temp in t1:
	print temp

#set
print "set"
set1 = {1,2,3,4}
print set1
set1.discard(5) #不存在时不报错，remove报错
print set1
print frozenset(set1) #frozenset转为不可修改的set

# == 判断是否值相同 is 判断地址是否相同

print len(u"中文")
print len(u"中文".decode("utf-8"))

print u"中文"

#文件
with open("a.txt","w") as f:
	f.write("this is a file test demo\n这是第二行")
with open("a.txt") as f:
	for line in f:
		print line.decode()
	print u"文件名称：%s,文件读写属性：%s"%(f.name,f.mode)
with open("a.txt") as f:
	print f.read().decode()#read全部读取，readline按行读取，readlines读取所有行，返回list

#文件属性
file_stat = os.stat("a.txt")
print time.localtime(file_stat.st_ctime)

#eval exec
r = eval("3+4")
print r
exec "print 'exec'"

#format
print "my name is {0},i am {1}".format("zhangsan",11)
print "my name is {name},i am {age}".format(name="lisi",age=12)
list = ["a1234","b1234","c1234"]
print "a={0[0]},b={0[1]},c={0[2][0]}".format(list)
print "PI is {m.pi},platform is {0.platform}".format(sys,m=math)




















