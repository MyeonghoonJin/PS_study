"""
팩토리얼 0의 개수 - s5
수학
"""

n = int(input())

# 5의 약수 개수
# 2의 약수 개수는 항상 5의 약수 개수보다 많을 수 밖에 없으므로 5의 약수 개수만 계산
divisor = 0

for i in range(1, n+1):
    # 5의 약수 개수
    while i % 5 == 0:
        i = i // 5
        divisor += 1

print(divisor)