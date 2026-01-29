"""
N과 M (5) - s3

"""
def solve():
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    current_path = []
    visited = [False] * 10001
    def backtracking(start):
        current_path.append(start)
        visited[start] = True
        # 종료 조건
        if len(current_path) == M:
            print(*current_path)
            visited[current_path.pop()] = False
            return
        # 순회
        for i in arr:
            if not visited[i]:
                backtracking(i)
        # 해당 순회가 끝났으면 다시 반환
        visited[current_path.pop()] = False
    for i in arr:
        backtracking(i)

if __name__ == '__main__':
    solve()