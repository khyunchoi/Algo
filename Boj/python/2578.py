bingo_list = []
for _ in range(5):
    bingo_list.append(list(map(int, input().split())))

call_list = []
for _ in range(5):
    tmp_list = list(map(int, input().split()))
    for i in tmp_list:
        call_list.append(i)

bingo = 0
for i in call_list:
    for j in range(5):
        for k in range(5):
            if bingo_list[j][k] == i:
                bingo_list[j][k] = 0

                total_row = 0
                for a in range(5):
                    total_row += bingo_list[j][a]
                if total_row == 0:
                    bingo += 1

                total_col = 0
                for a in range(5):
                    total_col += bingo_list[a][k]
                if total_col == 0:
                    bingo += 1
                
                if j == k:
                    total_diag1 = 0
                    for a in range(5):
                        total_diag1 += bingo_list[a][a]
                    if total_diag1 == 0:
                        bingo += 1

                if j + k == 4:
                    total_diag2 = 0
                    for a in range(5):
                        total_diag2 += bingo_list[a][4-a]
                    if total_diag2 == 0:
                        bingo += 1

                if bingo >= 3:
                    print(call_list.index(i) + 1)
                    exit()