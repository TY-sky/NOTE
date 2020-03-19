#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
print('---------------------------')
#count = 0
a = random.randint(1,10)
while True:
    temp = input('"写个字 猜猜看"')
    guess = int(temp)
    if guess == a:
        print('right')
        print('猜对也没用')
        break
    else:
        print('猜错')
        if guess < a:
            print('小了')
        else:
            print("大了")
     #   count = count +1
    
print('游戏"结束')
