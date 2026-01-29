"""
곱셈 - s1
분할 정복
"""
def solve():
    A,B,C = map(int,input().split())

    def multsquare(A,B,C):
        if B == 1:
            return A % C
        if B % 2 == 0:
            return ((multsquare(A,B // 2,C)) ** 2) % C
        else:
            return ((A % C) * multsquare(A,(B - 1) // 2,C) ** 2) % C
    print(multsquare(A,B,C))
if __name__ == '__main__':
    solve()
