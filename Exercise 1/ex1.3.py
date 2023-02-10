'''
Filename: ex1.3.py
Course: ENSF 338
Group Number: 12

This program implements of a version of the given code using
memoisation to improve performance.

'''
def func(n):
    def func_memo(n, m):
        
        #default cases (first two Fibancci numbers)
        if n in m:
            return m[n]

        #if n is not 1 or 2, store the value of the nth Fibonacci number in the dictionary m
        n_number = func_memo(n-1, m) + func_memo(n-2, m)
        m[n] = n_number
        return n_number

    
    # m is a dictionary to store the nth Fibonacci number. It initially contains the first 2 numbers of the sequence
    m = {0: 1, 1: 1}
    return func_memo(n, m)





