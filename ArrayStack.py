#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from Array import Array
from AbstractStack import AbstractStack


class ArrayStack(AbstractStack):
    """基于数组的栈实现"""
    DEFAULT_CAPACITY = 10  #默认大小

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    def __iter__(self):
        """实现迭代。从底到顶弹出"""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError("栈现在是空的，不能返回值！")
        return self._items[len(self)-1]

    def clear(self):
        """重置一个空的栈"""
        self._size = 0
        self._items =  Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """向栈顶压入一个值"""
        phy_lth = len(self._items)  #物理大小
        lgc_lth = len(self)         #逻辑大小
        if lgc_lth == phy_lth:
            """如果满了，此时需要扩展数组的长度"""
            newArray = Array(phy_lth*2)
            for count in range(phy_lth):
                newArray[count] = self._items[count]
            self._items = newArray
            self._items[lgc_lth] = item
            self._size += 1
        else:
            self._items[len(self)] = item
            self._size += 1

    def pop(self):
        """弹出栈顶的数据"""
        if self.isEmpty():
            raise KeyError("栈现在是空的，不能弹出值！")
        olditem = self._items[len(self) - 1]
        self._size -= 1

        if self._size < len(self._items)/3:
            newarray = Array(len(self._items)/2)
            for i in range(self._size):
                newarray[i] = self._items[i]
            self._items = newarray
        return olditem