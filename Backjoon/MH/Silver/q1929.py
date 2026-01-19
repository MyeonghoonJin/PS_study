"""
소수 구하기 - s3
에라토스테네스의 체
"""

m,n = map(int,input().split())

def prime(start,end):
    result = []
    arr = [True]*(end+1)
    # 0, 1 은 미리 제외
    arr[0] = False
    arr[1] = False

    # i는 소수, j는 i의 배수로 제외할 인덱스
    for i in range(2,int(end** 0.5) + 1):
        # ***i의 배수를 제거하기 위해 탐색 간격을 i로 설정하자!!!!***
        for j in range(i * i,end + 1,i):
            if arr[j] and j % i == 0:
                arr[j] = False
    for i in range(end+1):
        if arr[i] and i >= start:
            result.append(i)
    return result

for i in prime(m,n):
    print(i)
