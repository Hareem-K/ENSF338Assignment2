'''
Filename: ex1.5.py
Course: ENSF 338
Group Number: 12

This code improves its performance on the input given in point 2
'''

import matplotlib.pyplot as plt
import sys
import json
import timeit
import threading
threading.stack_size(33554432)

sys.setrecursionlimit(20000)

#Original
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

#Improved
import random

def optimized_func1(arr, low, high):
    while low < high:
        pivot = optimized_func2(arr, low, high)
        if pivot - low < high - pivot:
            optimized_func1(arr, low, pivot - 1)
            low = pivot + 1
        else:
            optimized_func1(arr, pivot + 1, high)
            high = pivot - 1

def optimized_func2(array, start, end):
    pivot_index = (start + end) // 2
    pivot = array[pivot_index]
    array[pivot_index], array[end] = array[end], array[pivot_index]
    partition_index = start
    i = start
    while i < end:
        if array[i] <= pivot:
            array[i], array[partition_index] = array[partition_index], array[i]
            partition_index += 1
        i += 1
    array[end], array[partition_index] = array[partition_index], array[end]
    return partition_index



with open("ex2.json", "r") as file:
    array = json.load(file)

times = []
timesimproved = []

for i in array:
        time = timeit.timeit(lambda: func1(i, 0, len(i) - 1), number = 1)
        times.append(time)

for i in array:
        time2 = timeit.timeit(lambda: optimized_func1(i, 0, len(i) - 1), number = 1)
        timesimproved.append(time2)

length = [len(i) for i in array]
    
plt.plot(length, times, label="Original")
plt.plot(length, timesimproved, label="Improved")
plt.xticks(length)
plt.title("Timing Results")
plt.xlabel("Length of List")
plt.ylabel("Time (s)")
plt.legend(loc="best")
plt.show()
