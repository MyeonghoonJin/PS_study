"""
수 복원하기 - s3
에라토스테네스의 체
"""

T = int(input())

def prime(n):
    result = []
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False

    for i in range(2,int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i,n + 1, i):
                prime[j] = False

    for i in range(2,n + 1):
        if prime[i]:
            result.append(i)
    return result

def find_prime(n):
    result = []
    prime_arr = prime(n)
    cnt_arr = [0] * len(prime_arr)
    for i in range(len(prime_arr)):
        while n != 1 and n % prime_arr[i] == 0:
            n = n / prime_arr[i]
            cnt_arr[i] = cnt_arr[i] + 1

    for j in range(len(cnt_arr)):
        if cnt_arr[j] >= 1:
            result.append((prime_arr[j],cnt_arr[j]))

    return result
N = []
for i in range(T):
    N.append(int(input()))
for num in N:
    for prime_num,exp in find_prime(num):
        print(prime_num,exp)