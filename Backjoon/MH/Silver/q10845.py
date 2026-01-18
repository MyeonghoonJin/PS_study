"""
큐 - s4
큐
"""
from collections import deque

n = int(input())
result = []
queue = deque()
def push(x):
    queue.append(x)

def pop():
    if len(queue) == 0:
        return -1
    return(queue.popleft())

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def front():
    if len(queue) == 0:
        return -1
    return queue[0] 

def back():
    if len(queue) == 0:
        return -1
    return queue[-1]

for _ in range(n):
    cmd = input()
    
    if cmd[:4] == "push":
        op, x = cmd.split()
        push(x)
    elif cmd == "pop":
        result.append(pop())
    elif cmd == "size":
        result.append(size())
    elif cmd == "empty":
        result.append(empty())
    elif cmd == "front":
        result.append(front())
    else:
        result.append(back())

for i in result:
    print(i)

    