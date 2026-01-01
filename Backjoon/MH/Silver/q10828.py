"""
스택
"""
import sys
input = sys.stdin.readline

n = int(input())
commanders = []
stack = []

for _ in range(n):
    command = input()
    commanders.append(command)

def push(x):
    stack.append(x)

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    return 0
def pop():
    if empty():
        return -1
    return stack.pop()
def top():
    if empty():
        return -1
    return stack[-1]

for command in commanders:
    match(command.strip().split()):
        case ["push", x]:
            push(x)
        case ["pop"]:
            print(pop())
        case ["size"]:
            print(size())
        case ["empty"]:
            print(empty())
        case ["top"]:
            print(top())