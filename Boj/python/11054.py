def lis(n):
    if results[n]:
        return results[n]

    tmp = 0
    for i in range(n):
        if arr[i] < arr[n]:
            tmp = max(tmp, lis(i))
    
    results[n] = tmp + 1

    return results[n]


def lis_reverse(n):
    if results_reverse[n]:
        return results_reverse[n]

    tmp = 0
    for i in range(n+1, N):
        if arr[i] < arr[n]:
            tmp = max(tmp, lis_reverse(i))
    
    results_reverse[n] = tmp + 1

    return results_reverse[n]


N = int(input())
arr = list(map(int, input().split()))
results = [0 for _ in range(N)]
results_reverse = [0 for _ in range(N)]

for i in range(N):
    lis(i)
    lis_reverse(i)

result = 0
for i in range(N):
    result = max(result, results[i]+results_reverse[i]-1)

print(result)