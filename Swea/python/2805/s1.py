import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            result += farm[i][j]

    for i in range(N):
        for j in range(N):
            if i + j < N//2 or i + j > (N//2 + N - 1):
                result -= farm[i][j]
                result -= farm[N-1-i][j]

    print('#{} {}'.format(tc, result))