"""
체스판 다시 칠하기 - s3

"""
def solve():
    # m = 행의 개수, n = 열의 개수
    m,n = map(int,input().split())
    arr = [input() for _ in range(m)]
    result = [[],[]]
    # x~x+7,y~y+7 사이의 체스판에서 최솟값
    def minVal(x,y,char):
        # B,W
        minValue = 0
        # B 패턴
        if char == 'B':
            for i in range(x,x+8):
                for j in range(y,y+8):
                    # 좌표 합이 짝수인 경우 B인지 확인
                    if (i + j) % 2 == 0:
                        if arr[i][j] != "B":
                            minValue += 1
                    else:
                        if arr[i][j] != "W":
                            minValue += 1
        # W 패턴
        if char == 'W':
            for i in range(x,x + 8):
                for j in range(y,y + 8):
                    # 좌표 합이 짝수인 경우 W인지 확인
                    if (i + j) % 2 == 0:
                        if arr[i][j] != "W":
                            minValue += 1
                    else:
                        if arr[i][j] != "B":
                            minValue += 1
        return minValue
    # B 패턴
    for i in range(m - 7):
        for j in range(n - 7):
            result[0].append(minVal(i, j, "B"))
    # W 패턴
    for i in range(m - 7):
        for j in range(n - 7):
            result[1].append(minVal(i, j, "W"))
    print(min(min(result[0]),min(result[1])))

if __name__ == "__main__":
    solve()