# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 20:36
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : quadratic.py
# @Software: PyCharm

import math


def quadratic(a, b, c):
    if a == 0 and b != 0:
        x = -c / b
        return x
    elif a != 0 and b == 0:
        return math.sqrt((-c) / a)
    elif a == 0 and b == 0:
        if c == 0:
            return 0
        else:
            return False
    elif b ** 2 - 4 * a * c >= 0 and b ** 2 + 4 * a * c >= 0:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b + math.sqrt(b ** 2 + 4 * a * c)) / (2 * a)
        return x1, x2
    else:
        print("b ** 2 - 4 * a * c < 0 或者 b ** 2 + 4 * a * c < 0")
        return False


a = float(input("请输入a："))
b = float(input("请输入b："))
c = float(input("请输入c："))

print('quadratic(a, b, c) =', quadratic(a, b, c))
