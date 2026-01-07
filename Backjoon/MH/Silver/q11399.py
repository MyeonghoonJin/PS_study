"""
ATM
"""
n = int(input())

time = list(map(int,input().split()))

time.sort()
waiting_time = []
result = 0

for i in range(n):
    if i == 0:
        waiting_time.append(time[i])
    else:
        waiting_time.append(time[i] + waiting_time[i-1])
print(sum(waiting_time))