"""
이항계수 - b1
조합
"""
def solve():
    n,k = map(int, input().split())
    comb = 1
    for i in range(1,k + 1):
        comb *= n - i + 1
        comb //= i
    print(comb)

if __name__ == '__main__':
    solve()