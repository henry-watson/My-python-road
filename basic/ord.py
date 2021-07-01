#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-09-14 20:54:19
# @Author  : Henry Watson
# @Link    : https://github.com/henry-watson/
# @Software: Sublime Text 3


import os
car = "BMW"
for car_char in car:
	char=ord(car_char)
	if char == 87:
		break;
	else:
		print(chr(char))

