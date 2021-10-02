import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                i_tmp = i
                i_cnt = 0
                while i_tmp < N and arr[i_tmp][j]:
                    i_cnt += 1
                    i_tmp += 1
                j_tmp = j
                j_cnt = 0
                while j_tmp < N and arr[i][j_tmp]:
                    j_cnt += 1
                    j_tmp += 1
                result.append([i_cnt, j_cnt])

                for x in range(i, i_tmp):
                    for y in range(j, j_tmp):
                        arr[x][y] = 0

    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    print('#{} {}'.format(tc, len(result)), end=' ')
    for res in result:
        print(*res, end=' ')
    print()