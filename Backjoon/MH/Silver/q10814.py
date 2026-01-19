"""
나이순 정렬 - s5
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    arr.append([age, name])
arr.sort(key = lambda x: x[0])

for i in arr:
    print(i[0], i[1])
