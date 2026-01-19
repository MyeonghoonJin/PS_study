"""
덩치 - s5
"""
n = int(input())

arr = []

for i in range(n):
    x,y = map(int, input().split())
    arr.append([x,y,1])
for i in range(n):
    for j in range(n):
        if i != j:
            # 다른 사람의 키 몸무게가 전부 큰 경우
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                arr[i][2] += 1
seq = [x[2] for x in arr]
print(*seq)
