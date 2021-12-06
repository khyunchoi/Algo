def calc(s):
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o'],
        ['p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k'],
        ['l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '.'],
    ]

    i0, j0, i1, j1 = 0, 0, 0, 0
    for i in range(3):
        for j in range(9):
            if s[0] == keyboard[i][j]:
                i0 = i
                j0 = j
            if s[1] == keyboard[i][j]:
                i1 = i
                j1 = j

    return abs(i0 - i1) + abs(j0 - j1)


def solution(s):
    answer = 0
    N = len(s) - 1
    words = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):
        words[0][j] = calc(s[j:j+2])
        answer += words[0][j]

    for i in range(1, N):
        for j in range(N):
            if i+j < N:
                words[i][j] = words[i-1][j] + words[0][i+j]
                answer += words[i][j]

    return answer


print(solution("abcc"))
print(solution("tooth"))
print(solution("zzz"))