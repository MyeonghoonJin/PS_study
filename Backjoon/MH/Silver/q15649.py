"""
N과 M(1) - s3
"""

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(i + 1)


def backtracking(current_perm,visited,nums):
    global m,n
    # 종료 조건
    if len(current_perm) == m:
        for i in current_perm:
            print(i,end=" ")
        print()
        return
    # 순회
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            current_perm.append(nums[i])
            backtracking(current_perm,visited,nums)
            # 순회 끝난 노드 제거
            current_perm.pop()
            # 방문 기록 복구
            visited[i] = False

# 방문한 자리
visited = [False]*len(arr)

backtracking([],visited,arr)