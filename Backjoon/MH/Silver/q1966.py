"""
프린터 큐 - s3
큐
"""
from collections import deque
T = int(input())

result = deque()
"""
input
    target = 타겟 인덱스
    list = 우선순위 리스트(deque)
output
    타겟의 인쇄 순서
"""
def printerQueue(target,list):
    cnt = 0
    
    while len(list) > 0:
        # 인쇄 성공
        if max(list) <= list[0]:
            # 타겟인 경우
            if target == 0:
                cnt += 1
                return cnt
            # 타겟이 아닌 경우
            list.popleft()
            target -= 1
            cnt += 1
        # 인쇄 실패
        else:
            temp = list.popleft()
            list.append(temp)
            # 타겟 차례인 경우 마지막 인덱스로 변경
            if target == 0:
                target = len(list) - 1
            # 타겟 차례가 아닌 경우 앞으로 한 칸 씩 당기기
            else:
                target -= 1
    return cnt
            
for _ in range(T):
    n, target = map(int,input().split())
    priority = deque(map(int,input().split()))
    result.append(printerQueue(target,priority))

for i in result:
    print(i)