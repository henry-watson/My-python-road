# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 19:32
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : Fibonacci sequence.py
# @Software: PyCharm

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def count(n):
    for i in range(0, n):
        print(fib(i), end='    ')
        # print(fib(i).reverse, end='    ')


num = int(input("请输入一个数字："))
count(num)