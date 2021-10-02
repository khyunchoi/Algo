import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort(reverse=True)

    result = 0
    for i in range(K):
        result += scores[i]

    print('#{} {}'.format(tc, result))