#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Name = input('输入你的名字\n')
Name = 'sx'
print('你的名字',Name)

if Name == 'sx' :
    print('YES')
else:
    print('名字错了')

print('hello,%s' %100)
height = 1.75
weight = 57
bmi = weight/(height*height)
if bmi <18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')
height = 1.69
weightmin = height*height*18.5
weightmax = height*height*25
print(weightmin,weightmax)

n1= 255
n2 = 1000
a= hex(n1)
print(a)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

import math
math.sqrt(2)

def quadratic(a, b, c):
    return ((-b+math.sqrt(b*b-4*a*c))/(2*a)),((-b-math.sqrt(b*b-4*a*c))/(2*a))




print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0): 
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

def calc(*numbers,sum):
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,sum= 2))

def power(a,n = 2):
    sum = 1
    while n>0:
        n = n-1
        sum = sum*a
    return sum

print(power(2,3))
print(calc(1,2,3,4,3,sum =3))

def product(*x):
    if  x == ():
        raise TypeError('bad operand type1')
    s =1
    for n in x:
        s = n*s
    return s

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else :
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3,'A','B','C')
'''
def trim(s):
    n = 0
    m = -1
    print(n,m)
    l = len(s)
    if l == 0 :
        return ''
    while (s[1:] == ' ' ) :
        n = n+1
        if n >l-1 :
            return ''
        print(n)
    while (s[m] == ' '):
        m = m-1
        l = l-1
        if l <0:
            return ''
        print(m)
    print(n,m,l)
    print(s[n:l])
    return s[n:l]
'''
def trim(s):
    if len(s) == 0:
        return ''
    while s[0] == ' ':
        s = s[1:]
        if len(s) == 0:
            return ''
        #print(1)
    while s[-1] ==' ':
        s = s[:-1]
        if len(s) == 0:
            return ''
        #print(2)
    print(s)
    return s




# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')


def findMinAndMax1(L):
    if L == []:
        print(L)
        return (None, None)
    max = L[0]
    min = L[0]
    for x in L:
        if x>max:
            max = x
        if x<min:
            min = x
    return (min,max)


def findMinAndMax(*L):    
    i = []
    print (L)
    if L == ([],):
        return None,None
    for x in L:        
        i.append(min(x))        
        i.append(max(x))    
    print (i)
    return tuple(i)
    
print(findMinAndMax([5,3,4,5,100,2312,4,124,51]))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

print(list(range(1,1)))
print(list(range(1)))
print(list(range(1,0)))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')





#L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = [x.lower() for x in L1 if isinstance(x,str)]


def normalize(name):
    a = ''
    for x,v in enumerate(name):
        if x == 0:
            a = v.upper()
        else :
            a = a +v.lower()
    return a

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def prod(L):    
    def f(x,y):
        return x * y 
    return reduce(f,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def is_palindrome1(n):
    if (n/10) < 1 :
        return True
    else :
        a = 1
        while n / 10**a >= 1:
            a = a + 1
       # print(a)
        for l in range(a):
            x =(n//10**l)%10  
            y = (n//10**(a-1-l))%10
            if n == 11:
                print(x,y)
            if x  !=  y :
                return False
        return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 10000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(s):
    return s[0]

def by_score(s):
    return -s[1]



L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)

a = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
b = a.values

def createCounter1():
	list1 = [0]
	def counter():
		list1[0] = list1[0] + 1
		return list1[0]
	return counter

def createCounter2():
    s = 0
    def counter():
        nonlocal s
        s = s +1
        return s 
    return counter

def createCounter():
    s = 0
    def counter():
        nonlocal s
        s = s +1
        return s 
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L)


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender
    
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width
        

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Chain(object):
    count = 0
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self,a):
        Chain.count = Chain.count +1
        return Chain('%s/%s+%s' % (self._path ,a,Chain.count))

    def __str__(self):
        return self._path

    __repr__ = __str__

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student1('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')