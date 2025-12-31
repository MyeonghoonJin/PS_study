n = int(input())

arr = []
for i in range(n):
    str = input()
    arr.append(str)

result = ""
# 글자 수만큼 반복
for i in range(len(arr[0])):
    char = arr[0][i]
    # n만큼 반복
    for j in range(n):
        if arr[j][i] != arr[0][i]:
            char = "?"
    result += char
print(result)