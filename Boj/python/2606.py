def dfs(n):
    global result

    visited[n] = 1

    for i in range(N+1):
        if not visited[i] and graph[n][i] == 1:
            result += 1
            visited[i] = 1
            dfs(i)


N = int(input())
M = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(1)

print(result)