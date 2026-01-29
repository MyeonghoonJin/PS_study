"""
RGB거리 - s1
DP
"""
def solve():
    N = int(input())
    dp = [0,0,0]
    for i in range(1,N + 1):
        r,g,b = map(int, input().split())
        dp = [
            r + min(dp[1],dp[2]),
            g + min(dp[0],dp[2]),
            b + min(dp[0],dp[1])
        ]
    print(min(dp))
if __name__ == '__main__':
    solve()