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
def improvedfunc1(arr, low, high):
    if low < high:
        pi = improvedfunc2(arr, low, high)
        improvedfunc1(arr, low, pi-1)
        improvedfunc1(arr, pi + 1, high)

def improvedfunc2(array, start, end):
    p = array[(start + end) // 2]

    array[end - 1], array[(start + end) // 2] = array[(start + end) // 2], array[end - 1]

    low = start
    high = end - 1
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[end - 1], array[high] = array[high], array[end - 1]
    return high

with open("ex2.json", "r") as file:
    array = json.load(file)

times = []
timesimproved= []

for i in array:
        time = timeit.timeit(lambda: func1(i, 0, len(i) - 1), number = 1)
        times.append(time)

for i in array:
        time2 = timeit.timeit(lambda: improvedfunc1(i, 0, len(i) - 1), number = 1)
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
