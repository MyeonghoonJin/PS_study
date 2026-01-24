"""
최소 힙 - s2

"""
import sys
from collections import deque
input = sys.stdin.readline
def solve():
    # 최소 힙
    arr = deque()
    def insert(x):
        arr.append(x)
        idx_x = len(arr) - 1
        while True:
            if idx_x == 0:
                break
            # 부모 노드와 비교
            if arr[(idx_x - 1) // 2] > arr[idx_x]:
                arr[(idx_x - 1) // 2],arr[idx_x] = arr[idx_x],arr[(idx_x - 1) // 2]
                idx_x = (idx_x - 1) // 2
            else:
                return
    def delete():
        if arr:
            result = arr.popleft()
            # 배열이 없는 경우
            if not arr:
                return result
            # 맨 마지막 노드 최상단으로 이동
            arr.rotate(1)
            idx = 0

            while True:
                left_idx = idx * 2 + 1
                right_idx = idx * 2 + 2
                # 말단 노드인 경우 종료
                if left_idx > len(arr) - 1:
                    return result
                # 자식 노드가 2개인지 1개인지 판단
                if right_idx <= len(arr) - 1:
                    # 자식 노드 수에 따른 비교
                    min_child_idx = right_idx if arr[left_idx] > arr[right_idx] else left_idx
                else:
                    min_child_idx = left_idx
                # 더 작은 자식 노드와 교환
                if arr[idx] > arr[min_child_idx]:
                    arr[idx],arr[min_child_idx],idx = arr[min_child_idx],arr[idx],min_child_idx
                else:
                    return result
        # 힙이 빈 경우
        else:
            return 0
    n = int(input())
    for _ in range(n):
        cmd = int(input())
        if cmd != 0:
            insert(cmd)
        else:
            print(delete())
# 파이썬 라이브러리 풀이
import heapq
def solve2():
    heap = []
    n = int(input())
    for _ in range(n):
        cmd = int(input())
        if cmd != 0:
            heapq.heappush(heap,cmd)
        else:
            print(heapq.heappop(heap) if heap else 0)

if __name__ == '__main__':
    solve2()