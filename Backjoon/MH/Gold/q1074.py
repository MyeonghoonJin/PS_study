"""
Z - g5
분할정복
"""
def solve():
    N,r,c = map(int,input().split())

    def binary_search_row(row):
        cnt = 0
        l = 0
        r = 2 ** N - 1
        mid = (l + r) // 2
        for i in range(N):
            mid = (l + r) // 2
            if row <= mid:
                r = mid
            else:
                l = mid + 1
                cnt += 2 ** (2 * N - 1 - 2 * i)
        return cnt
    def binary_search_col(col):
        cnt = 0
        l = 0
        r = 2 ** N - 1
        mid = (l + r) // 2
        for i in range(N):
            mid = (l + r) // 2
            if col <= mid:
                r = mid
            else:
                l = mid + 1
                cnt += 2 ** (2 * N - 2 - 2 * i)
        return cnt

    print(binary_search_row(r) + binary_search_col(c))

# 재귀 및 분할 정복
def solve2():
    N,r,c = map(int,input().split())

    def sol(N,r,c):

        if not N:
            return 0
        half = 2 ** (N - 1)
        # 4사분면
        if r >= half and c >= half:
            return 3 * half ** 2 + sol(N - 1, r - half, c - half)
        # 3사분면
        elif r >= half and c < half:
            return 2 * half ** 2 + sol(N - 1, r - half, c)
        # 2사분면
        elif r < half and c >= half:
            return half ** 2 + sol(N - 1,r,c - half)
        # 1사분면
        else:
            return sol(N - 1,r,c)

    print(sol(N,r,c))

if __name__ == "__main__":
    solve2()