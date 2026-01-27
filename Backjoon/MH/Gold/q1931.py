"""
회의실 배정 - g5
그리디 알고리즘
"""
import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    arr = []
    cnt = 0
    for _ in range(n):
        a,b = map(int,input().split())
        arr.append([a,b])
    # 끝나는 시간으로 정렬
    arr.sort(key = lambda x:(x[1],x[0]))
    # 직전 끝나는 시간
    prev_end = 0
    for idx,val in enumerate(arr):
        s = val[0]
        e = val[1]
        if s >= prev_end:
            prev_end = e
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    solve()