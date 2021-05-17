#DSA-Tryout

import sys

sys.setrecursionlimit(10000)   #This is to overcome default python recursion limit

def fibonacci(num):
    for i in range(3, num+1):
        memo.update({i:memo[i-1] + memo[i-2]})
    return memo[num]

memo={1:1, 2:1} #global dictionary to store the fibonacci number already computed
print("Fibonacci number:",fibonacci(6))
print(memo)
