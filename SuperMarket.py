#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""队列实现，模拟超市的收银过程"""
import random
from Node import Node
from AbstractCollection import AbstractCollection


class LinkedQueue(AbstractCollection):
    def __init__(self, sourceCollection=None):
        self._front = self._rear = None
        AbstractCollection.__init__(self, sourceCollection)

    def add(self,item):
        newitem = Node(item)
        if self.isEmpty():
            self._front = newitem
        else:
            self._rear.next = newitem
        self._rear = newitem
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("队列为空不能弹出")
        olditem = self._front.data
        self._front = self._front.next
        if self._front == None:
            self._rear = None
        self._size -= 1
        return olditem

    def clear(self):
        self._front = self._rear = None
        self._size = 0

    def __iter__(self):
        head = self._front
        while head != None:
            yield head.data
            head = head.next


    def peek(self):
        if self.isEmpty():
            raise KeyError("队列现在是空的")
        return self._front.data

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


class Cashier:
    def __init__(self):
        self._totalCustomerwaitTime = 0
        self._customerServed = 0
        self._currentCustomer =None
        self._queue = LinkedQueue()

    def addCustomer(self, c):
        self._queue.add(c)

    def serveCustomers(self, currentTime):
        if self._currentCustomer is None:
            #没有顾客就返回
            if self._queue.isEmpty():
                return
            else:
                #弹出顾客，计算时间
                self._currentCustomer = self._queue.pop()
                self._totalCustomerwaitTime += currentTime - self._currentCustomer.arrivalTime()
                self._customerServed += 1

            #进行服务
            self._currentCustomer.serve()
            #服务完成，空闲
            if self._currentCustomer.amountOfServiceNeeded() == 0:
                self._currentCustomer = None

    def __str__(self):
        result = "Total for the cashier\n"+"Number of customers served:"+str(self._customerServed)+"\n"
        if self._customerServed != 0:
            aveWaitTime = self._totalCustomerwaitTime / self._customerServed
            result += "Number of customers left in queue:"+str(len(self._queue))+"\n"\
                      +"Average time customers spend\n"+"waiting to be served:"+"%5.2f"%aveWaitTime
        return result


class Customer:
    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival, arrivalTime, averageTimePerCustomer):
        if random.random() <= probabilityOfNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None

    def __init__(self, arrivalTime, serviceNeeded):
        self._arrivalTime = arrivalTime
        self._amountOfServiceNeeded = serviceNeeded

    def arrivalTime(self):
        return self._arrivalTime

    def amountOfServiceNeeded(self):
        return self._amountOfServiceNeeded

    def serve(self):
        self._amountOfServiceNeeded -= 1


def main():
    print("Welcome to the Market Simulator!\n")
    lengthOfSimulation = int(input("Enter the total running time: "))
    averageTimePerCus = int(input("Enter the average processing time per customer: "))
    probabilityOfNewArrival = float(input("Enter the probability of a new arrival: "))
    if lengthOfSimulation < 1 or lengthOfSimulation > 1000:
        print("Running time must be an integer greater than 0" + \
              "\nand less than or equal to 1000")
    elif averageTimePerCus <= 0 or averageTimePerCus >= lengthOfSimulation:
        print("Average time per customer must be an integer" + \
              "\ngreater than 0 and less than running time")
    elif probabilityOfNewArrival <= 0 or probabilityOfNewArrival > 1:
        print("Probability must be geater than 0" + \
              "\nand less than or equal to 1")
    else:
        model = MarketModel(lengthOfSimulation, averageTimePerCus,
                            probabilityOfNewArrival)
        model.runSimulation()
        print(model)

if __name__ == "__main__":
    main()