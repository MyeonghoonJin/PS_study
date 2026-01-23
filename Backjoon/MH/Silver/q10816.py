"""
숫자 카드 2 - s4
"""
from collections import Counter

def solve():
    n = int(input())
    arr_n = list(map(int, input().split()))
    m = int(input())
    arr_m = list(map(int, input().split()))

    # 각 원소의 개수 딕셔너리
    cnt = Counter(arr_n)

    for i in arr_m:
        print(cnt[i],end=" ")

if __name__ == "__main__":
    solve()