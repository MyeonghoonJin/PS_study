"""
블랙잭 - b2
브루트포스
"""
def solve():
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j != k and i != k:
                    if result < arr[i] + arr[j] + arr[k] <= m:
                        result = arr[i] + arr[j] + arr[k]
    print(result)

if __name__ == '__main__':
    solve()