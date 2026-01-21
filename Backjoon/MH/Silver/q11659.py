"""
구간 합 구하기 4
구간 합
"""
import sys
input = sys.stdin.readline
def solve():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    ranges = [list(map(int,input().split())) for _ in range(m)]

    prefix = [0]
    for i in arr:
        prefix.append(prefix[-1] + i)
    def range_sum(start,end):
        return prefix[end] - prefix[start - 1]

    for x,y in ranges:
        print(range_sum(x,y))

if __name__ == '__main__':
    solve()