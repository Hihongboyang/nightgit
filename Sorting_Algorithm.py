#!/usr/bin/env python 
# -*- coding:utf-8 -*-



def InsertSort(sequence):
    """直接插入排序"""
    for i in range(len(sequence)):
        #依次拿出数组中的数，和其前面的数比较。
        temp = sequence[i]
        j = i - 1
        while j>=0 and temp < sequence[j]:
            #如果temp小，就将sequence[j]向后移动
            sequence[j+1] = sequence[j]
            j -= 1
        #找到temp的位置后放入。
        sequence[j+1] = temp

def Half_fold_Insert(sequence, inser_seq):
    """半折插入排序
       这需要sequence是有序的，
       额外提供一个需要插入的序列inser_seq
    """
    for i in range(len(inser_seq)):
        #给定上下界限，确定半折的位置
        low = 0
        high = len(sequence) - 1
        temp = inser_seq[i]
        #如果low大于high说明找到了这个位置
        while low < high:
            mid = (low + high)//2
            if temp <= sequence[mid]:
                high = mid-1
            else:
                low = mid +1
        sequence.insert(high, temp)

def BubbleSort(sequence):
    """冒泡排序"""
    length = len(sequence)
    for i in range(length-1, -1 , -1):
        for j in range(i-1, -1, -1):
            if sequence[i] > sequence[j]:
                sequence[j], sequence[i] = sequence[i], sequence[j]

def QuickSort(sequence, left, right):
    if left < right:
        mid = partition(sequence, left, right)
        QuickSort(sequence, left, mid-1)
        QuickSort(sequence, mid+1, right)

def partition(sequence, left, right):
    temp = sequence[left]
    while left < right:
        while left < right and temp <= sequence[right]:
            right -= 1
        sequence[left] = sequence[right]
        while left < right and temp >= sequence[left]:
            left += 1
        sequence[right] = sequence[left]
    sequence[left] = temp
    return left




