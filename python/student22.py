#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'TY'

class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_gender(self):
        return self.__gender
		
    def set_gender(self,gender):
        if gender == 'male':
            self.__gender = gender 
        elif gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender') 
    			
lisa = Student('Lisa', 99,'female')
#bart = Student('Bart', 59,'male')
lisa.print_score()

# 测试:
bart = Student('Bart',66,'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
		
print(bart.get_gender())
