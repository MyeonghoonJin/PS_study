"""
N과 M(3) - s3
"""
n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(i + 1)

def backtracking(current_path):
    # 종료 조건
    if len(current_path) == m:
        print(*current_path)
        return
    # 순회
    for i in range(n):
        current_path.append(arr[i])
        backtracking(current_path)
        current_path.pop()

backtracking([])