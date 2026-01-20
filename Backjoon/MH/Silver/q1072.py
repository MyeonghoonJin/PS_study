"""
게임 - 실버3
"""

def solve():
    x, y = map(int, input().split())
    z = y * 100 // x

    if z >= 99:
        print(-1)
        return
    # n만큼 더 했을 경우 승률이 올라가는지 확인
    def isLarger(n):
        if (y + n) * 100 // (x + n) > z:
            return True
        else:
            return False
    search_range = 1
    # n에 2를 곱해 승률이 올라가는 n을 빠르게 찾음
    while True:
        if isLarger(search_range):
            break
        else:
            search_range *= 2
    # n이 아무리 커도 이진 탐색을 하면 시간 초과는 뜰 수가 없음
    l = 0
    r = search_range
    mid = 0
    while l <= r:
        mid = (l + r) // 2
        # 정답 조건
        if mid == 0 or (isLarger(mid) and not isLarger(mid - 1)):
            break
        if isLarger(mid):
            r = mid - 1
        else:
            l = mid + 1
    # 정답이 0일 수 없으므로 mid가 0인 경우는 반드시 1임
    print(mid if mid != 0 else 1)


if __name__ == '__main__':
    solve()