#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-01 18:30:32
# @Author  : Henry Watson
# @Link    : https://github.com/henry-watson/
# @Software: Sublime Text 3


#if 语句
a = 1
while a < 7:
	if (a%2==0):
		print(a,"is even")
	else:
		print(a,"is odd")
	a+=1


#引入生成随机数的模块
import random
#程序设定生成 1-20 之间的一个随机数，让用户猜
secretNum = random.randint(1,20)

print("这是一个位于 1-20 之间的数")
#设定用户只能猜 3 次
for number in range(1,4):
    print("请输入猜测的数：")
    guess = int(input())
    if guess <= 1:
        break
    if guess < secretNum:
        print("太小啦")
    elif guess > secretNum:
        print("太大啦")
    else:
        break
if(guess == secretNum):
    print("真厉害，猜对啦，就是",str(guess))
else:
    print("很遗憾，正确的答案应该是",str(secretNum))
