"""
게임 - 실버3
"""
import sys
n,m = map(int,input().split())

rate = int(m / n * 100)

r = 10**10
l = 0
mid = (r + l) // 2

if rate >= 99:
    print(-1)
    sys.exit()

while r >= l:
    mid = (r + l) // 2
    # 승률이 2퍼이상 오른 경우
    if rate + 1 < int((m + mid) / (n + mid) * 100):
        r = mid - 1
    # 승률이 오르지 않은 경우
    elif rate == int((m + mid) / (n + mid) * 100):
        l = mid + 1
    # 승률이 1퍼만 오른 경우
    else:
        if mid == 0:
            r += 1
            mid += 1
        # 최솟값이 아닌 경우 -> 축소 필요
        elif rate + 1 == int((m + mid - 1) / (n + mid - 1) * 100):
            r = mid - 1
        # 바로 직전값까지 승률이 0퍼 상승인 경우
        elif rate == int((m + mid - 1) / (n + mid - 1) * 100):
            print(mid)
            sys.exit()
print(mid)