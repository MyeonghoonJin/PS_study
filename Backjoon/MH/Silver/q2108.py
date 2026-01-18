"""
통계학 - s2

"""
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

def mode(sorted_arr):
    val_arr = []
    for idx,val in enumerate(sorted_arr):
        if idx > 0 and val == sorted_arr[idx-1]:
            val_arr[-1][1] += 1
        else:
            val_arr.append([val,1])

    val_arr.sort(key = lambda x:(x[1],x[0]))
    max_val = max(x[1] for x in val_arr)

    temp = []

    for i in val_arr:
        if i[1] == max_val:
            temp.append(i[0])

    if len(temp) > 1:
        return temp[1]
    else:
        return temp[0]

# 산술기하
print(round(sum(arr) / len(arr)))
# 정렬
arr.sort()
# 중앙값
print(arr[len(arr)//2])
# 최빈값
print(mode(arr))
# 범위
print(arr[len(arr) - 1] - arr[0])