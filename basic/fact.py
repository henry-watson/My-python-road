# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 21:22
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : fact.py
# @Software: PyCharm

def fact(n):
    if n == 1:
        return 1
    elif n>1:
        return n * fact(n - 1)
    else:
        return False


# fact(-3)

print(fact(4))
