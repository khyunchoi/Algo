N = int(input())

dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))

max_total = 0

#첫번째 주사위의 밑면 1부터 6까지의 케이스 시행
for i in range(1, 7):
    pick_list = [i]
    idx = 0
    j = i

    while idx < N:
        if dices[idx].index(j) == 0:
            number = dices[idx][5]
            pick_list.append(number)
        elif dices[idx].index(j) == 1:
            number = dices[idx][3]
            pick_list.append(number)
        elif dices[idx].index(j) == 2:
            number = dices[idx][4]
            pick_list.append(number)
        elif dices[idx].index(j) == 3:
            number = dices[idx][1]
            pick_list.append(number)
        elif dices[idx].index(j) == 4:
            number = dices[idx][2]
            pick_list.append(number)
        else:
            number = dices[idx][0]
            pick_list.append(number)
        
        j = number
        idx += 1

    # 각 케이스에서의 옆면 최댓값 구하기
    total = 6 * N
    for i in range(N):
        if pick_list[i] == 6:
            total -= 1
            if pick_list[i+1] == 5:
                total -= 1
        elif pick_list[i] == 5:
            if pick_list[i+1] == 6:
                total -= 2
        elif pick_list[i+1] == 6:
            total -= 1

    # 1부터 6까지 케이스의 최댓값들 중 가장 큰값 구하기
    if max_total < total:
        max_total = total

print(max_total)