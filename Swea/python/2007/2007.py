T = int(input())

for tc in range(1, T+1):
    words = input()

    for i in range(1, 11):
        if words[0:i] == words[i:2*i]:
            print('#{} {}'.format(tc, i))
            break