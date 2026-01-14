"""
소수 찾기 - b2
소수
"""

n = int(input())

arr = list(map(int,input().split()))


result = 0

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in arr:
    if isPrime(i):
        result += 1

print(result)