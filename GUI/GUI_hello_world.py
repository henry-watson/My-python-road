# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 0:58
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : GUI_hello_world.py
# @Software: PyCharm

import wx
app = wx.App()
frame = wx.Frame(None,-1,"hello world")
frame.Show(True)
app.MainLoop()
