"""
N과 M(4) - s3
"""

n,m = map(int, input().split())

arr = []

def backtracking(start):
    # 종료 조건
    if len(arr) == m:
        print(*arr)
        return
    #순회
    for i in range(start,n + 1):
        arr.append(i)
        backtracking(i)
        arr.pop()

backtracking(1)
