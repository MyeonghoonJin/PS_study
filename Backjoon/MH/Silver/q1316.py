def IsGroupWord(str):
    isCountedChar = []
    for i in range(len(str)):
        #첫번째 원소 처리
        if i == 0 or str[i] not in isCountedChar:
            isCountedChar.append(str[i])
        elif str[i] == str[i - 1]:
            continue    
        else:
            return False
    return True

n = int(input())

arr = []
result = 0

for _ in range(n):
    str = input()
    if IsGroupWord(str):
        result += 1

print(result)

    
