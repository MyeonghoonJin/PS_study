"""
팰린드롬수 - b1

"""
def solve():
    arr = []
    while True:
        k = int(input())
        if k == 0:
            break
        arr.append(k)

    def palindrome(num):
        string = str(num)
        for idx in range(0,(len(string) + 1) // 2):
            if string[idx] != string[-1 - idx]:
                return False
        return True

    for num in arr:
        if palindrome(num):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solve()