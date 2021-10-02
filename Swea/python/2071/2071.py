T = int(input())

for tc in range(T):
    total = 0
    numbers_list = list(map(int, input().split()))

    for i in numbers_list:
        total += i;

    avg = total / len(numbers_list)

    print(f'#{tc + 1} {round(avg)}')