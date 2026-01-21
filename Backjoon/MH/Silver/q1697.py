"""
숨바꼭질 - s1
BFS
"""
from collections import deque
def solve():
    n,m = map(int,input().split())

    def bfs(start,target):
        result = 0
        visited = set()
        prevqueue = deque([start])
        nextqueue = deque()
        while True:
            # 깊이 + 1
            if not prevqueue:
                result += 1
                prevqueue = nextqueue.copy()
                nextqueue.clear()
            current_node = prevqueue.popleft()
            visited.add(current_node)
            # 완료 조건
            if current_node == target:
                break
            if current_node + 1 not in visited and current_node + 1 in range(0,1000001):
                nextqueue.append(current_node + 1)
            if current_node - 1 not in visited and current_node - 1 in range(0,1000001):
                nextqueue.append(current_node - 1)
            if current_node * 2 not in visited and current_node * 2 in range(0,1000001):
                nextqueue.append(current_node * 2)
        return result
    print(bfs(n,m))
if __name__ == '__main__':
    solve()