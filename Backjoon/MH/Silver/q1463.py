import sys
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