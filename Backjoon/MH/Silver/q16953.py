"""
A -> B - s2
BFS, 그리디
"""
from collections import deque
def solve():
    s,e = map(int, input().split())
    prev_queue = deque()
    prev_queue.append(s)
    next_queue = deque()
    cnt = 0
    while prev_queue:
        # e를 발견한 경우
        if e in prev_queue:
            print(cnt + 1)
            return
        q = prev_queue.popleft()
        # 도착지를 넘어선 경우 조기 종료
        if q * 2 <= e:
            next_queue.append(q * 2)
        if q * 10 + 1 <= e:
            next_queue.append(q * 10 + 1)
        # prev_queue를 다 소비한 경우
        if not prev_queue:
            cnt += 1
            prev_queue = next_queue.copy()
            next_queue.clear()
    # e를 못 찾은 경우
    print(-1)
    return

if __name__ == '__main__':
    solve()