#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from AbstractCollection import AbstractCollection


class AbstractStack(AbstractCollection):
    """一个抽象栈的实现"""
    def __init__(self, sourceCollection=None):
        AbstractCollection.__init__(self, sourceCollection)

    def add(self, item):
        """添加项目"""
        self.push(item)

