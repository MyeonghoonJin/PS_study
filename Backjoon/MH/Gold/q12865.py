"""
평범한 배낭 - g5
DP , 0-1 배낭문제
"""
def solve():
    N, K = map(int, input().split())
    val = [0]
    weight = [0]
    for _ in range(N):
        m, v = map(int, input().split())
        # m은 무게, v는 가치
        val.append(v)
        weight.append(m)
    # dp[n][k] -> n개까지 물건이 주어졌을 때 k 용량에 담을 수 있는 최대가치값
    # n번째 물건을 담을 경우 -> dp[n][k] = max(val[n] + dp[n - 1][k - m],dp[n - 1][k])
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    # n번째 물건의 가치, 무게
    for i in range(1, N + 1):
        # 해당 물건의 무게, 가치
        m = weight[i]
        v = val[i]
        # j는 가방에 남은 공간
        for j in range(0, K + 1):
            # 넣을 수 없으면
            if m > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # 물건을 담을 수 있는 경우 담았을 때와 담지 않았을 때 최댓값
                dp[i][j] = max(dp[i - 1][j -  m] + v,dp[i - 1][j])
    print(dp[N][K])
if __name__ == "__main__":
    solve()
