"""
최고의 집합 - lv3
"""
from math import ceil
def solution(n, s):
    answer = []

    def maxmult(n, s):
        if n == 1:
            answer.append(s)
            return
        q = ceil(s / n)
        while s > q:
            q = ceil(s / n)
            answer.append(q)
            s -= q
            n -= 1
        maxmult(n, s)

    if n > s:
        answer.append(-1)
        return answer

    else:
        maxmult(n, s)
        answer.sort()
    return answer
