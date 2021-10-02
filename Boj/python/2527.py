for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    x_list = [x1, x2, x3, x4]
    y_list = [y1, y2, y3, y4]

    x_list.sort()
    y_list.sort()
    
    judge_list = []
    for i in range(4):
        judge_list.append([0, 0, 0, 0])

    for i in range(x_list.index(x1), x_list.index(x2)+1):
        for j in range(y_list.index(y1), y_list.index(y2)+1):
            judge_list[i][j] += 1

    for i in range(x_list.index(x3), x_list.index(x4)+1):
        for j in range(y_list.index(y3), y_list.index(y4)+1):
            judge_list[i][j] += 1

    count_2 = 0
    for i in range(4):
        for j in range(4):
            if judge_list[i][j] == 2:
                count_2 += 1
    
    if count_2 == 0:
        print('d')
    elif count_2 == 1:
        print('c')
    elif count_2 <= 3:
        print('b')
    elif count_2 > 4:
        print('a')
    else:
        isB = False
        for i in range(4):
            for j in range(4):
                if judge_list[i][j] == 2:
                    row_sum = 0
                    for k in range(4):
                       row_sum += judge_list[i][k]
                    if row_sum == 8:
                        isB = True

                    col_sum = 0
                    for k in range(4):
                        col_sum += judge_list[k][j]
                    if col_sum == 8:
                        isB = True
        
        if isB:
            print('b')
        else:
            print('a')
