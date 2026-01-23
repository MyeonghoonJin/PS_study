"""
카드2 - s4
큐
"""
from collections import deque
def solve():
    n = int(input())
    arr = deque([x for x in range(1,n + 1)])
    while len(arr) > 1:
        arr.popleft()
        arr.append(arr.popleft())
    print(*arr)

if __name__ == "__main__":
    solve()