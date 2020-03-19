#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'TY'



fpath = r'C:\py\test.ini'

with open(fpath, 'a') as f:
    f.write('Hello, world!')


with open(fpath, 'r') as f:
    s = f.read()
    print(s)