"""
삼각형 만들기 - s3
"""
import sys
input = sys.stdin.readline

n = int(input())

len_arr = []
for _ in range(n):
    len_arr.append(int(input()))

## 시간 복잡도 : O(nlog n)
len_arr.sort()

for i in range(n - 2):
    # 선택된 빗변의 길이가 바로 다음으로 큰 두 변의 크기 합보다 작아서 삼각형을 이루는 경우
    if len_arr[-1 - i] < len_arr[-2 - i] + len_arr[-3 - i]:
        print(len_arr[-1 - i] + len_arr[-2 - i] + len_arr[-3 - i])
        sys.exit()
print(-1)