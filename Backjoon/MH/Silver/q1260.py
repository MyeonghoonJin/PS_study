"""
DFS와 BFS - s2
DFS,BFS,그래프
"""
from collections import deque
import sys
input = sys.stdin.readline
def solve():
    N,M,V = map(int,input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        x,y = map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)
    visited = [False] * (N + 1)
    def dfs(v):
        visited[v] = True
        print(v,end=' ')
        for i in sorted(adj[v]):
            if not visited[i]:
                dfs(i)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            q = queue.popleft()
            print(q,end=' ')
            for i in sorted(adj[q]):
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    dfs(V)
    print()
    visited = [False] * (N + 1)
    bfs(V)

if __name__ == '__main__':
    solve()