"""
좌표 정렬하기 - s5
정렬
"""

def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[0], x[1]))
    for i in arr:
        print(i[0], i[1])
if __name__ == "__main__":
    solve()
