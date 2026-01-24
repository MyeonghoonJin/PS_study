"""
색종이 만들기 - s2

"""
def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 흰색, 파란색
    colors = [0,0]
    # 크기, 시작 좌표
    def paper(n,x,y):
        if n == 1:
            colors[1 if arr[x][y] == 1 else 0] += 1
            return
        c = [0,0]
        for i in range(n):
            for j in range(n):
                if arr[x + i][y + j] == 0:
                    c[0] += 1
        c[1] = n ** 2 - c[0]
        # 종료 조건
        if c[0] == n ** 2:
            colors[0] += 1
            return
        elif c[1] == n ** 2:
            colors[1] += 1
            return
        # 재귀 함수
        else:
            dx = [0,n // 2,0,n // 2]
            dy = [0,0,n // 2,n // 2]
            for i in range(4):
                paper(n // 2,x + dx[i],y + dy[i])

    paper(n,0,0)
    print(*colors,sep = "\n")


if __name__ == "__main__":
    solve()