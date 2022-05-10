"""
File name : guessNum.py
Program IDE : PyCharm
Create file time: 2022/5/10 21:03
File Create By Author : pc
"""

import random
import sys

# 生命次数
lives = 3
# 随机数字
number = range(1, 11)
secret_num = random.choice(number)
# 机会次数初始值为1
guess_choice = 1
# 判断次数是否超出游戏次数
while guess_choice <= lives:
    choice_num = input("please input your guessing num in 1~10:")
    if int(choice_num) >= 1 and int(choice_num) <= 10:
        if int(choice_num) == secret_num:
            print("Congulalations!!!")
            break
        else:
            print("you have {} counts".format(lives - guess_choice))
            guess_choice += 1
    # 当输入的数超出游戏范围
    else:
        print("please input num in 1~10")
        print("you have {} counts".format(lives-guess_choice))
        guess_choice += 1
    continue
else:
    print("Failed,your choice is used,the secret number is :{} ".format(secret_num))
    sys.exit()
