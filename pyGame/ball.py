# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 13:19
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : ball.py
# @Software: PyCharm

# 导入库
import pygame,sys
# 初始化pygame和参数
pygame.init()
width = 800
height = 600
speed = [1,1]
Black = (0,0,0)
fps = 6
fClock = pygame.time.Clock()

# 设置窗体
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ball")
# 导入ball图像和获取ball的外切矩形
ball = pygame.image.load("./PYG02-ball.gif")
ballrect = ball.get_rect()
# 循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 外切矩形按速度移动
    ballrect = ballrect.move(speed[0],speed[1])
    # 判断ball是否超出边界，超出则按-speed速度反弹
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    # 窗口将窗体涂满黑色，因为ball移动后，原位置默认填充白色，fill使用RGB填充
    screen.fill(Black)
    # *将ball绘制到ballrect上
    screen.blit(ball,ballrect)
    # 窗口刷新
    pygame.display.update()
    fClock.tick(fps)
