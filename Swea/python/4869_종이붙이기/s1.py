import sys
sys.stdin = open('input.txt')


def paper(n):
    idx = n//10
    f = [1, 3]
    for i in range(2, idx):
        f.append(2 * f[i-2] + f[i-1])

    return f[idx-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, paper(N)))