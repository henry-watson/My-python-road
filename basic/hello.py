"""
File name : hello.py
Program IDE : PyCharm
Create file time: 2022/5/10 20:42
File Create By Author : pc
"""

def fib(n):
    a = 1
    b = 1
    while a <= n:
        print(a,end=",")
        a,b = b,a+b

fib(1024)
