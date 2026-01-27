"""
트리의 부모 찾기 - s2
트리,그래프 이론,BFS
"""
import sys
from collections import deque

input = sys.stdin.readline
def solve():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    visited[1] = True
    p = [-1] * (N + 1)
    for _ in range(N - 1):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    # 작업 큐
    queue = deque()
    queue.append(1)
    while queue:
        v = queue.popleft()
        for i in adj[v]:
            if not visited[i]:
                visited[i] = True
                p[i] = v
                queue.append(i)
    for i in range(2,N + 1):
        print(p[i])

if __name__ == '__main__':
    solve()