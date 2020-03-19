#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, functools
def metric(text):
    if isinstance(text,str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                start = time.time()
                a = fn(*args, **kw)
                end = time.time()
                sp= end -start 
                print('%s %s in %s ms' % (fn.__name__, text,sp))
                return a
            return wrapper
        return decorator
    else :
        @functools.wraps(text)
        def wrapper(*args, **kw):
            start = time.time()
            a = text(*args, **kw)
            end = time.time()
            sp= end -start 
            print('%s executed in %s ms' % (text.__name__, sp))
            return a
        return wrapper





# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric('ex')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败1!',f)
elif s != 7986:
    print('测试失败!')


print(fast.__name__)