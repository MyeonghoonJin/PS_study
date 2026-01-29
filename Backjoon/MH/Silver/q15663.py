"""
N과 M (9) - s2

"""
def solve():
    N, M = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    # 인덱스로 방문 노드 판단
    visited = [False] * N
    current_path = []
    result = []
    def backtracking(node,idx):
        current_path.append(node)
        visited[idx] = True
        # 종료 조건
        if len(current_path) == M:
            print(*current_path)
            visited[idx] = False
            current_path.pop()
            return
        # 순회 (중복 값은 없이)
        prev = -1
        for i,val in enumerate(arr):
            if not visited[i] and val != prev:
                backtracking(val,i)
                prev = val
        # 백트래킹
        visited[idx] = False
        current_path.pop()
    # 중복 없이 호출
    seen = set()
    for i,val in enumerate(arr):
        if val not in seen:
            seen.add(val)
            backtracking(val,i)

if __name__ == '__main__':
    solve()