def judge(i, j, k):
    for a in range(i, i+k):
        for b in range(j, j+k):
            if a >= N or b >= N:
                return False
            
            if paper[a][b] == 0:
                return False
    
    return True


def colored(i, j, k, num):
    for a in range(i, i+k):
        for b in range(j, j+k):
            paper[a][b] = num


def backtracking(cnt):
    global result

    if result <= 25 - sum(arr[1:]):
        return

    if cnt == 0:
        result = min(result, 25 - sum(arr[1:]))
        return

    for i in range(N):
        for j in range(N):
            if paper[i][j] == 1:
                for k in range(5, 0, -1):
                    if judge(i, j, k) and arr[k] > 0:
                        arr[k] -= 1
                        colored(i, j, k, 0)
                        backtracking(cnt - k**2)
                        colored(i, j, k, 1)
                        arr[k] += 1
                return


N = 10
paper = [list(map(int, input().split())) for _ in range(N)]
arr = [0, 5, 5, 5, 5, 5]
result = 25

tmp = 0
for i in range(N):
    for j in range(N):
        if paper[i][j] == 1:
            tmp += 1

backtracking(tmp)

if result == 25:
    result = -1

print(result)
