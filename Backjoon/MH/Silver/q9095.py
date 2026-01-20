"""
1, 2, 3 더하기

"""
def solve1():
    T = int(input())
    result = []
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    def divisors(n):
        count = 0
        div3 = n // 3
        for i in range(div3 + 1):
            r = n - 3 * i
            div2 = r // 2
            for j in range(div2 + 1):
                div1 = r - 2 * j
                # 중복 순열 공식
                count += factorial(div1 + j + i) // (factorial(div1) * factorial(j) * factorial(i))
        return count

    for i in range(T):
        n = int(input())
        result.append(divisors(n))
    print(*result , sep='\n')

def solve2():
    T = int(input())
    arr = [0,1,2,4]
    result = []
    for i in range(4,11):
        arr.append(arr[i-1] + arr[i-2] + arr[i-3])

    for x in range(T):
        result.append(arr[int(input())])
    print(*result , sep='\n')

if __name__ == '__main__':
    solve2()