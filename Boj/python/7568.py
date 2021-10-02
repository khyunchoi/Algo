N = int(input())
peoples = [list(map(int, input().split())) for _ in range(N)]

result = []
cnt = 0
for people in peoples:
    cnt = 1
    for another_people in peoples:
        if people[0] < another_people[0] and people[1] < another_people[1]:
            cnt += 1

    result.append(cnt)

print(*result)