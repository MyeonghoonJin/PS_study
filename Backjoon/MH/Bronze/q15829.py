"""
Hashing - b2
"""

l = int(input())
str = input().strip()
chars = list(str)

result = 0
r = 31
M = 1234567891

for idx,char in enumerate(chars):
    #소문자 알파벳의 고유값
    char_value = ord(char) - ord('a') + 1
    result += char_value * (r ** idx)
print(result % M)