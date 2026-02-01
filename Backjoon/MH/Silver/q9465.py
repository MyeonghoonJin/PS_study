"""
스티커 - s1
DP
"""
import sys
input = sys.stdin.readline
def solve():
    T = int(input())
    result = []
    for _ in range(T):
        N = int(input())
        arr = []
        for _ in range(2):
            arr.append(list(map(int,input().split())))
        dp = [[] for _ in range(N)]
        # dp[i][0] => ox / dp[i][1] = xo / dp[i][2] = xx
        # dp[0]
        dp[0] = [arr[0][0],arr[1][0],0]
        for i in range(1,N):
            dp[i] = [
                # 해당 열의 선택이 ox, 직전 선택은 xo/xx 중 더 큰값
                max(dp[i - 1][1] + arr[0][i],dp[i - 1][2] + arr[0][i]),
                # 해당 열의 선택이 xo, 직전 선택은 ox/xx 중 더 큰값
                max(dp[i - 1][0] + arr[1][i],dp[i - 1][2] + arr[1][i]),
                # 해당 열의 선택이 xx, 직전 선택은 ox/xo/xx 중 더 큰값
                max(dp[i - 1])
            ]
        result.append(max(dp[N - 1]))
    print(*result,sep = '\n')

if __name__ == '__main__':
    solve()
