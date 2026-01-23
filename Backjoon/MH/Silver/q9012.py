"""
괄호 - s4
"""
import sys
def solve():

    n = int(input())
    input_val = [sys.stdin.readline().rstrip('\n') for _ in range(n)]
    def vps(x):
        # 길이가 홀수이면 no
        if len(x) % 2 != 0:
            return False
        while len(x) > 0:
            s = "()"
            # () 전부 제거
            if s in x:
                x = x.replace(s, "")
            else:
                return False
        return True

    for x in input_val:
        if vps(x):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()