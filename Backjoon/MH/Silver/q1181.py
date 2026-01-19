"""
단어 정렬 - s5

"""
n = int(input())
arr = []
strings = []
lenset = set()
for _ in range(n):
    str = input()
    length = len(str)
    lenset.add(length)
    arr.append((length,str))

lenset = list(lenset)

arr.sort()

# 더미 데이터 추가
arr.append((-1,'dummy'))
lenset.append(0)

sorted_strings = []
j = 0
temp = []
for length,str in arr:
    if length == lenset[j]:
        temp.append(str)
        continue
    temp.sort()
    for x in temp:
        sorted_strings.append(x)
    temp.clear()
    temp.append(str)
    j += 1
# 중복 제거
sorted_strings = list(dict.fromkeys(sorted_strings))
for i in sorted_strings:
    print(i)