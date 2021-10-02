T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    my_list = []
    for _ in range(N):
        my_list.append(list(map(int, input().split())))

    max_total = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    total += my_list[x][y]
            
            max_total = max(max_total, total)

    print(f'#{tc+1} {max_total}')