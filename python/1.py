#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'TY'




sum = 0
for x in range(101):
    sum = sum + x
print(sum)
print('''line1
line2
line3''')
s=ord('中')
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print(s)
test = ['1','2','3',]
test.append('Adam')
test.insert(1, 'Jack')
test.pop(0)
for xx in test:
    print(xx)
def power(x):
    return x * x
a = power(5)
print(a)
from functools import reduce
xx = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(xx)

def is_deng(a,b):
    if a == b:
	    return 1
    else:
        return 0
		
def is_palindrome(n):
    a = str(n)
    num = len(a)
    if num == 1:
	    s = 1
    elif num == 2:
	    s = is_deng(a[0],a[1])
    elif num == 3:
        s = is_deng(a[0],a[2])
    return s 
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
	
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[1]
L2 = sorted(L, key=by_name)
print(L2)	

def createCounter():   
    count = [0]
    def counter():       
        count[0] += 1
        return count[0]
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))	
print(L) 

