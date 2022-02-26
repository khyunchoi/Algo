def dfs(depth):
    global result

    if depth == N:
        result += 1
        return
    
    for i in range(N):
        arr[depth] = i
        if not visited[i] and possible(depth):
            visited[i] = 1
            dfs(depth+1)
            visited[i] = 0


def possible(now):
    for i in range(now):
        if arr[i] == arr[now]:
            return False
        elif abs(i - now) == abs(arr[i] - arr[now]):
            return False
    return True


N = int(input())
arr = [0 for _ in range(N)]
visited = [0 for _ in range(N)]
result = 0

dfs(0)

print(result)