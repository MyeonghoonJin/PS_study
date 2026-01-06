"""
# https://www.acmicpc.net/problem/2579
"""
import sys
input = sys.stdin.readline
n = int(input())
scores = []
scores.append(0)


for _ in range(n):
    s = int(input())
    scores.append(s)

maxScore = []
maxScore.append(0)
if n == 1:
    print(scores[1])
    sys.exit()
if n == 2:
    print(scores[1] + scores[2])
    sys.exit()
if n > 2:
    maxScore.append(scores[1])
    maxScore.append(scores[1] + scores[2])

    for i in range(3,n + 1):
        maxScore.append(
            max(maxScore[i-2] + scores[i],maxScore[i-3] + scores[i-1] + scores[i])
        )
    print(maxScore[n])