"""
집합 - s5
"""
import sys
import array
input = sys.stdin.readline
testSet = set()

def solve():
    def check(x):
        if x in testSet:
            return True
        else:
            return False
    def add(x):
        testSet.add(x)
    def remove(x):
        if check(x):
            testSet.remove(x)
    def toggle(x):
        if x in testSet:
            remove(x)
        else:
            add(x)
    def empty():
        testSet.clear()
    def all():
        for i in range(1,21):
            add(i)

    n = int(input())

    # -128~127 범위의 정수만 허용, 0,1 을 넣을 때 효율 좋음
    result = array.array('b')
    for i in range(n):
        cmd = input()
        match (cmd.strip().split()):
            case ["add", x]:
                add(int(x))
            case ["check", x]:
                if check(int(x)):
                    result.append(1)
                else:
                    result.append(0)
            case ["remove",x]:
                remove(int(x))
            case ["toggle",x]:
                toggle(int(x))
            case ["all"]:
                all()
            case ["empty"]:
                empty()
    for i in result:
        print(i)

if __name__ == "__main__":
    solve()