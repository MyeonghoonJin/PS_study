
n = int(input())

arrN = set(map(int, input().split()))

m = int(input())

arrM = list(map(int, input().split()))

for i in range(m):
    if arrM[i] in arrN:
        print(1)
    else:
        print(0)