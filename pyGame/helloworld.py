# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 13:06
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : helloworld.py
# @Software: PyCharm

import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("hello world")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()