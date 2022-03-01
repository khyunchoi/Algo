def lis(n):
    if results[n]:
        return results[n]

    tmp = 0
    for i in range(n):
        if arr[i] < arr[n]:
            tmp = max(tmp, lis(i))
    
    results[n] = tmp + 1

    return results[n]


N = int(input())
arr = list(map(int, input().split()))
results = [0 for _ in range(N)]

results[0] = 1

result = 0
for i in range(N):
    result = max(result, lis(i))

print(result)