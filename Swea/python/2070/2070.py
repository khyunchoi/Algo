T = int(input())

for tc in range(T):
    num = list(map(int, input().split()))

    a = num[0]
    b = num[1]
    if a > b:
        print(f'#{tc + 1} >')
    elif a == b:
        print(f'#{tc + 1} =')
    else:
        print(f'#{tc + 1} <')
