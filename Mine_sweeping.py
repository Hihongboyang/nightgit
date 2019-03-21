#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class BlockStatus:
    normal = 1  #未点击
    opened = 2  #已点击
    mine = 3    #地雷
    flag = 4    #标记为地雷
    ask = 5     #标记为问好
    bomb = 6    #踩中地雷
    hint = 7    #被双击的周围
    double = 8  #正被鼠标左右键点击

class Mine:
    def __init__(self, x, y, value=0):
        self._x = x
        self._y = y
        self._value = 0
        self._around_mine_count = -1
        self._status = BlockStatus.normal
        self.set_value(value)

    def __repr__(self):
        return str(self._value)