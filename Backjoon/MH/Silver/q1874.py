"""
스택 수열
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = []
stack = []
result = []
ops = []

for _ in range(n):
    m = int(input())
    arr.append(m)

idx_arr = 0
idx = 0

while idx_arr < n:
    if len(stack) == 0 or stack[-1] != arr[idx_arr]:
        # 더 이상 push할 수 있는 수가 없는데 pop의 조건이 안 맞는 경우 NO를 출력
        if idx == n:
            print("NO")
            sys.exit()
        stack.append(idx + 1)
        ops.append("+")
        idx += 1
    elif stack[-1] == arr[idx_arr]:
        idx_arr += 1
        result.append(stack.pop())
        ops.append("-")

for i in ops:
    print(i)
