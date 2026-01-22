"""
좌표 압축
값 압축
"""
def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    arr = [(arr[idx],idx)  for idx in range(n)]
    sorted_arr = sorted(arr, key=lambda x: x[0])
    shufled_idx = [i[1] for i in sorted_arr]
    cnt_arr = [0]
    for i in range(1,n):
        # 다른 값이 나올때마다 누적해서 더하기
        if sorted_arr[i - 1][0] != sorted_arr[i][0]:
            cnt_arr.append(cnt_arr[i - 1] + 1)
        else:
            cnt_arr.append(cnt_arr[i - 1])
    indexed_cnt_arr = [[cnt_arr[i],shufled_idx[i]] for i in range(n)]
    sorted_cnt_arr = sorted(indexed_cnt_arr, key=lambda x: x[1])
    result = [x[0] for x in sorted_cnt_arr]
    print(*result)

if __name__ == '__main__':
    solve()