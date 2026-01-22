"""
나무 자르기 - s2
이분 탐색 - 최댓값 찾기
"""
def solve():
    n,m = map(int,input().split())
    trees = list(map(int,input().split()))

    # O(n)
    def total(h):
        total_len = 0

        for tree in trees:
            if tree > h:
                dif = tree - h
                total_len += dif
        return total_len

    # 이분 탐색 - 최댓값 찾기
    l = 0
    r = max(trees)
    mid = 0
    while l < r:
        mid = (l + r + 1) // 2
        if total(mid) >= m:
            l = mid
        else:
            r = mid - 1
    print(r)
if __name__=='__main__':
    solve()
