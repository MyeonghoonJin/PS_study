"""
OX퀴즈 - b2

"""
def solve():
    n = int(input())
    result = []
    for i in range(n):
        str = input()
        extra_score = 0
        arr1 = str[:-1]
        arr2 = str[1:]
        score = 0
        for i in range(len(arr1)):
            if arr1[i] == arr2[i] and arr1[i] == 'O':
                extra_score += 1
                # 추가 점수
                score += extra_score
            else:
                # 추가 점수 초기화
                extra_score = 0
        # 기본 점수
        for i in str:
            if i == 'O':
                score += 1
        result.append(score)
    print(*result,sep='\n')


if __name__ == '__main__':
    solve()