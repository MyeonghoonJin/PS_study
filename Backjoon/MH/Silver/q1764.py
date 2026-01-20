"""
듣보잡 - s4
"""
import sys
input = lambda : sys.stdin.readline().strip()

def solve():

    n,m = map(int,input().split())
    result = []
    arr_n = []
    arr_m = []
    for i in range(n):
        arr_n.append(input())
    for i in range(m):
        arr_m.append(input())

    # 크기 비교
    min_arr_len = min(m,n)
    # 이진 탐색을 위한 정렬 : O(NlogN)
    if n < m:
        arr_m.sort()
    else :
        arr_n.sort()
    # 이진 탐색 함수
    def binary_search(arr,target):
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if target < arr[mid]:
                r = mid - 1
            elif target > arr[mid]:
                l = mid + 1
            else:
                return target
        return False
    # 더 적은 배열의 원소마다 공통 원소 확인
    for i in range(min_arr_len):
        if m > n:
            if binary_search(arr_m,arr_n[i]):
                result.append(binary_search(arr_m, arr_n[i]))
        else:
            if binary_search(arr_n,arr_m[i]):
                result.append(binary_search(arr_n, arr_m[i]))

    result.sort()
    print(len(result))
    print(*result,sep='\n')

if __name__ == '__main__':
    solve()