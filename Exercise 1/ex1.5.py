'''
Filename: ex1.5.py
Course: ENSF 338
Group Number: 12

This program times the original code and our improved version, for all integers between 0 and 35,
and plots the results.

'''

import time
import matplotlib.pyplot as plt

#original given function
def original_func(n):
    if n == 0 or n == 1:
        return n

    else:
        return original_func(n-1) + original_func(n-2)

#improved function from part 6    
def improved_func(n):
    def func_memo(n, m):

        if n in m:
            return m[n]

        n_number = func_memo(n-1, m) + func_memo(n-2, m)
        m[n] = n_number
        return n_number

    m = {0: 1, 1: 1}
    return func_memo(n, m)

# Time the original function
original_times = []
for i in range(36):
    start = time.time()
    original_func(i)
    end = time.time()
    original_times.append(end - start)
    
# Time the improved function
improved_times = []
for i in range(36):
    start = time.time()
    improved_func(i)
    end = time.time()
    improved_times.append(end - start)

# Plot the results
plt.plot(original_times, label='Original Code', color='darkmagenta')
plt.plot(improved_times, label='Improved Code', color='lightcoral')
plt.xlabel('Input (n)')
plt.ylabel('Time (s)')
plt.title("Time Comparison of Original and Improved Code")
plt.legend()
plt.show()
