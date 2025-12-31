n = int(input())

for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))

for i in range(n - 1):
    print(" " * (n - 1 - (i + 1)) + "*" * ((i + 2) * 2 - 1))