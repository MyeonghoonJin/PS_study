"""
구간 합 구하기 5 - s1
누적합
"""
import sys
input = sys.stdin.readline
def solve():
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    targets = [list(map(int,input().split())) for _ in range(M)]
    prefix = [[] for _ in range(N)]
    prefix[0].append(arr[0][0])
    # 누적 합 구하기
    for i in range(N):
        for j in range(N):
            # 0번째 행
            if i == 0 and i != j:
                prefix[i].append(prefix[i][j - 1] + arr[i][j])
            # 0번째 열
            elif j == 0 and j != i:
                prefix[i].append(prefix[i - 1][j] + arr[i][j])
            # 그 외의 좌표
            elif i != 0 and j != 0:
                prefix[i].append(prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j])
    for target in targets:
        x1 = target[0] - 1
        y1 = target[1] - 1
        x2 = target[2] - 1
        y2 = target[3] - 1
        result = prefix[x2][y2]
        # 일반적인 경우
        if x1 > 0 and y1 > 0:
            result -= prefix[x1- 1][y2]
            result -= prefix[x2][y1 - 1]
            result += prefix[x1 - 1][y1 - 1]
        # 시작점이 0번째 열
        elif x1 == 0 and y1 > 0:
            result -= prefix[x2][y1 - 1]
        # 시작점이 0번째 행
        elif x1 > 0 and y1 == 0:
            result -= prefix[x1 - 1][y2]
        print(result)
def solve2():
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    targets = [list(map(int,input().split())) for _ in range(M)]
    # N + 1 크기로 만들어서 0행/ 0열에 패딩 채우기
    prefix = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1,N + 1):
        for j in range(1,N+1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i - 1][j - 1]
    for target in targets:
        x1 = target[0]
        y1 = target[1]
        x2 = target[2]
        y2 = target[3]
        print(prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1])
if __name__ == '__main__':
    solve2()