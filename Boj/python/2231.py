N = int(input())

result = 0
for i in range(N):
    tmp = i
    tmp += sum(list(map(int, str(i))))

    if tmp == N:
        result = i
        break

print(result)