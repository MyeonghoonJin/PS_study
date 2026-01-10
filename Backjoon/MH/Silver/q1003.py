"""
피보나치 함수
"""
# import sys
# sys.setrecursionlimit(10000)

T = int(input())

arr = [] 

fib0Arr = [0] * 41
fib1Arr = [0] * 41

fib0Arr[0] = 1

fib1Arr[1] = 1


for _ in range(T):
    n = int(input())
  
    for i in range(n + 1):
        if i >= 2:
    
            fib0Arr[i] = fib0Arr[i - 1] + fib0Arr[i - 2]
            fib1Arr[i] = fib1Arr[i - 1] + fib1Arr[i - 2]

    arr.append((fib0Arr[n],fib1Arr[n]))

for x,y in arr:
    print(x,y)