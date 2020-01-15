# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 1:46
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : fig.py
# @Software: PyCharm

# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes