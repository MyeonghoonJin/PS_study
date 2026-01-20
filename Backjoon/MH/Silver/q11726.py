"""
2×n 타일링 - s3
DP
"""

def solve():
    n = int(input())
    arr = []
    # arr[0]
    arr.append(1)
    # arr[1]
    arr.append(1)
    if n > 1:
        for i in range(2,n + 1):
            arr.append(arr[i-1] + arr[i-2])
    print(arr[n] % 10007)


if __name__ == '__main__':
    solve()