"""
2×n 타일링 2 - s3
DP
"""

def solve():
    n = int(input())
    dp = []
    # dp[0]
    dp.append(1)
    # dp[1]
    dp.append(1)
    # dp[2:n+1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] * 2)
    print(dp[n] % 10007)

if __name__ == '__main__':
    solve()