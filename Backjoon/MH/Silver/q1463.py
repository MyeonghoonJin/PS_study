import sys

def solve1(n):
    n = int(input())

    visited = set()
    prevqueue = set()
    nextqueue = set()
    prevqueue.add(n)
    depth = 0

    while True:
        for num in prevqueue:
            if num == 1:
                print(depth)
                sys.exit(0)

            visited.add(num)
            if num % 3 == 0:
                nextqueue.add(num // 3)
            if num % 2 == 0:
                nextqueue.add(num // 2)
            nextqueue.add(num - 1)
        depth += 1
        prevqueue = nextqueue.copy()
        nextqueue.clear()

def solve2():
    n = int(input())
    dp = []
    # dp[0]
    dp.append(0)
    # dp[1]
    dp.append(0)
    # dp[2]
    dp.append(1)
    # dp[3]
    dp.append(1)
    for i in range(4, n + 1):
        temp = []
        # 3으로 나눠지는 경우
        if i % 3 == 0:
            temp.append(1 + dp[i // 3])
        # 2로 나눠지는 경우
        if i % 2 == 0:
            temp.append(1 + dp[i // 2])
        # 항상 적용 가능한 경우
        temp.append(1 + dp[i - 1])
        # 3가지 경우 중 최솟값
        dp.append(min(temp))

    print(dp[n])

if __name__ == '__main__':
    solve2()