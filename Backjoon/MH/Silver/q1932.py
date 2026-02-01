"""
정수 삼각형 - s1
DP
"""
def solve():
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dp = []
    # dp[0]
    dp.append([arr[0][0]])
    for i in range(1,N):
        tmp = []
        for col in range(i + 1):
            if col == 0:
                tmp.append(dp[i - 1][0] + arr[i][0])
            elif col == i:
                tmp.append(dp[i - 1][i - 1] + arr[i][i])
            else:
                tmp.append(max(dp[i - 1][col],dp[i - 1][col - 1]) + arr[i][col])
        dp.append(tmp)
    print(max(dp[N - 1]))
if __name__ == '__main__':
    solve()