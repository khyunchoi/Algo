def stairs(step):
    if result[step]:
        return result[step]
    
    result[step] = arr[step] + max(stairs(step - 3) + arr[step - 1], stairs(step - 2))

    return result[step]


N = int(input())
arr = []
result = [0 for _ in range(N)]

for _ in range(N):
    arr.append(int(input()))

result[0] = arr[0]
if len(result) > 1:
    result[1] = arr[0] + arr[1]
if len(result) > 2:
    result[2] = arr[2] + max(arr[0], arr[1])

stairs(N-1)

print(result[N-1])