"""
N과 M(2) - s3
"""

n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(i + 1)

def backtracking(current_path,arr,visited):
    global n,m
    # 종료 조건
    if len(current_path) == m and sorted(current_path) == current_path:
        for i in current_path:
            print(i,end=" ")
        print()
        return
    # 순회
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            current_path.append(arr[i])
            # visited[i] = False
            backtracking(current_path,arr,visited)
            # 순회 끝난 노드 제거
            current_path.pop()
            # # 방문 기록 복구
            visited[i] = False


# 방문한 자리
visited = [False]*len(arr)

backtracking([],arr,visited)


