def dfs(depth, tmp_arr):

    if depth == M:
        results.append(tmp_arr)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, tmp_arr + [arr[i]])
            visited[i] = 0


N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
visited = [0 for _ in range(len(arr))]
results = []
tmp_arr = []

dfs(0, tmp_arr)

for res in results:
    print(*res)