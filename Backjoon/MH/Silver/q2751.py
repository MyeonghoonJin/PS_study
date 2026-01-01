"""
수 정렬하기 2 
"""
import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    m = int(input())
    arr.append(m)

arr.sort()

for i in arr:
    print(i)