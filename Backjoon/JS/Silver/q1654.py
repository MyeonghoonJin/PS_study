import sys
input = sys.stdin.readline
k,n = map(int,input().split())

total = 0
arr = []
for i in range(k):
    d = int(input())
    arr.append(d)
    total += d
    

leftMaxN = 1
rightMaxN = max(arr)
midMaxN = rightMaxN

while rightMaxN - leftMaxN > 1:
    totalcnt = 0
    for i in arr:
        totalcnt += i // midMaxN
    
    # 몫의 합이 더 작다는 건 maxN이 최대값을 넘어갔다는 것 
    if totalcnt < n:    
        rightMaxN = midMaxN
        midMaxN = (rightMaxN + leftMaxN) // 2

    # 몫의 합이 n과 같거나 더 크다는건 maxN이 최대값이 아니라는 것
    else:
        leftMaxN = midMaxN
        midMaxN = (rightMaxN + leftMaxN) // 2


print(int(midMaxN))