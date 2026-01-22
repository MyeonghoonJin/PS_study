"""
쉬운 최단거리 - s1

"""
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    arr = []
    target_idx = []
    result = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    # 목표지점 탐색
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                target_idx.append(i)
                target_idx.append(j)
    # target = [x,y]
    def bfs(x0,y0,row,col):
        result = [[0] * col for _ in range(row)]
        visited = [[False] * col for _ in range(row)]
        queue = deque([(x0,y0)])
        while queue:
            x,y = queue.popleft()
            visited[x][y] = True

            if x + 1 < row and not visited[x + 1][y] and arr[x + 1][y] != 0:
                visited[x + 1][y] = True
                result[x + 1][y] = result[x][y] + 1
                queue.append((x + 1,y))
            if x > 0 and not visited[x - 1][y] and arr[x - 1][y] != 0:
                visited[x - 1][y] = True
                result[x - 1][y] = result[x][y] + 1
                queue.append((x - 1, y))
            if y + 1 < col and not visited[x][y + 1] and arr[x][y + 1] != 0:
                visited[x][y + 1] = True
                result[x][y + 1] = result[x][y] + 1
                queue.append((x,y + 1))
            if y > 0 and not visited[x][y - 1] and arr[x][y - 1] != 0:
                visited[x][y - 1] = True
                result[x][y - 1] = result[x][y] + 1
                queue.append((x, y - 1))
        for i in range(n):
            for j in range(m):
                # 시작지점이거나 접근 불가능 노드인 경우 제외
                if arr[i][j] == 0 or (i == x0 and j == y0):
                    continue
                if result[i][j] == 0:
                    result[i][j] = -1
        for row in result:
            print(*row)

    bfs(target_idx[0],target_idx[1],n,m)

if __name__ == "__main__":
    solve()