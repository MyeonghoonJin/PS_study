"""
요세푸스 문제0 s-4

"""

n,k = map(int,input().split())

arr = []
result = []
for i in range(n):
    arr.append(i + 1)


start = 0
while arr:
    start = (start + k - 1) % len(arr)
    result.append(arr.pop(start))
print(f"<{', '.join(map(str, result))}>")