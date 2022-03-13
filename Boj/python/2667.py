from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, b))

    results[count] = 0

    while q:
        i, j = q.popleft()

        if board[i][j] == 1:
            board[i][j] = count
            results[count] += 1

            for di, dj in dij:
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 1:
                    q.append((ni, nj))


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
count = 2
results = dict()
dij = ((-1, 0), (0, 1), (1, 0), (0, -1))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            bfs(i, j)
            count += 1

sorted_results = sorted(results.items(), key = lambda item: item[1])

print(len(results))

for result in sorted_results:
    print(result[1])