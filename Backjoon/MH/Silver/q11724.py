"""
연결 요소의 개수 - s2
그래프
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solve():
    N,M = map(int, input().split())
    V = [n for n in range(1,N+1)]
    # 인접 리스트
    adj = [[] for _ in range(N + 1)]
    cnt = 1
    for _ in range(M):
        x,y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    visited = [False] * (N + 1)
    visited[0] = True
    def dfs(node):
        visited[node] = True
        for y in adj[node]:
            if not visited[y]:
                dfs(y)
    start = 1
    while False in visited:
        dfs(start)
        if False in visited:
            start = visited.index(False)
            cnt += 1
    print(cnt)
if __name__ == '__main__' :
    solve()