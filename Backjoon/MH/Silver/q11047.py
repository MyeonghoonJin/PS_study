"""
동전0 - s4

"""
def solve():
    n,m = map(int,input().split())
    arr = []
    result = 0
    for i in range(n):
        arr.append(int(input()))

    while m != 0:
        # m < arr[-1] 인 경우
        if m < arr[-1]:
            arr.pop()
        else:
            result += m // arr[-1]
            m %= arr[-1]
            arr.pop()
    print(result)
if __name__ == '__main__':
    solve()