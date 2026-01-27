"""
토마토 - g5
BFS
"""
import sys
from collections import deque
input = sys.stdin.readline
def solve():
    M,N = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    starts = set()
    already = True
    # 이미 다 익어있는 경우
    for i in range(N):
        for j in range(M):
            # 시작 좌표 저장
            if arr[i][j] == 1:
                starts.add((i,j))
                visited[i][j] = True
            if already and arr[i][j] == 0:
                already = False
    if already:
        print(0)
        sys.exit()

    queue = deque()
    def count(x,y):
        current_val = arr[x][y]
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx,dy in dir:
            nx, ny = x + dx, y + dy
            # 인접점이 들어갈 수 없는 칸, 시작점인 칸, 범위 밖의 칸을 제외한 칸일 때만 수행
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1 and arr[nx][ny] != -1 and (nx,ny) not in starts and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                # x,y가 시작점인 경우
                if (x,y) in starts:
                    arr[nx][ny] = 1
                elif arr[nx][ny] == 0:
                    ## 이 부분이 BFS의 특성을 이해하지 못한 코드
                    arr[nx][ny] = current_val + 1

    for x,y in starts:
        queue.append((x,y))
    # BFS 탐색
    while queue:
        x,y = queue.popleft()
        count(x,y)
    max_val = 0
    for row in arr:
        for val in row:
            # 0이 존재하는 경우
            if val == 0:
                print(-1)
                sys.exit()
        max_val = max(max(row),max_val)
    print(max_val)
if __name__ == '__main__':
    solve()