#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""队列实现，模拟超市的收银过程"""

class MarketModel:
    def __init__(self, prob_newarr, lenth_simul, averagetime):
        self._prob_newarr = prob_newarr
        self._lenth_simul = lenth_simul
        self._averagetime = averagetime
        self._cashier = Cashier()

    def runSimulation(self):
        """运行一个时钟计时"""
        for currentTime in range(self._lenth_simul):
            #尝试产生一个顾客
            customer = Customer.generateCustomer(
                self._prob_newarr, currentTime, self._averagetime)
            #将成功产生的顾客发送给收银员
            if customer != None:
                self._cashier.addCustomer(customer)
            #安排其他服务单元
            self._cashier.serveCustomers(currentTime)

    def __str__(self):
        return str(self._cashier)

