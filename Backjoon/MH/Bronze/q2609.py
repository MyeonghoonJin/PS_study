"""
최대공약수와 최소공배수 - b1
유클리드 호제법
"""
def solve():
    n,m = map(int, input().split())
    # n > m 조건
    n, m = max(n, m), min(m, n)
    temp = n * m
    r1 = n % m
    # 최대 공약수
    while r1:
        n, m = m, r1
        r1 = n % m
    print(m)
    # 최대 공약수
    print(temp // m)

if __name__ == '__main__':
    solve()