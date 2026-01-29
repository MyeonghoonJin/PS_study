"""
가장 긴 증가하는 부분 수열 - s2
DP(정의 기반형)
"""
def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    # dp[0] = 0
    dp = []
    for i in range(N):
        tmp = []
        for j in range(i):
            if arr[j] < arr[i]:
                tmp.append(dp[j] + 1)
        dp.append(max(tmp) if tmp else 1)
    print(max(dp))

if __name__ == '__main__':
    solve()