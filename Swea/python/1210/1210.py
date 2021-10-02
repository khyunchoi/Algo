for tc in range(1, 11):
    N = int(input())

    ladders = [list(map(int, input().split())) for _ in range(100)]

    start = 0
    for i in range(100):
        if ladders[99][i] == 2:
            start = i
            break

    i = 99
    while i > 0:
        if start + 1 < 100 and ladders[i][start + 1] == 1:
            j = start + 1
            while j + 1 < 100 and ladders[i][j + 1] == 1:
                j += 1
            start = j
        elif start - 1 >= 0 and ladders[i][start - 1] == 1:
            j = start - 1
            while j - 1 >= 0 and ladders[i][j - 1] == 1:
                j -= 1
            start = j

        i -= 1

    # i = 99
    # while i > 0:
    #     if start == 0:
    #         if ladders[i][1] == 1:
    #             j = 1
    #             while ladders[i][j+1] == 1:
    #                 j += 1
    #                 if j == 99:
    #                     break
    #             start = j
    #     elif start == 99:
    #         if ladders[i][98] == 1:
    #             j = 98
    #             while ladders[i][j-1] == 1:
    #                 j -= 1
    #                 if j == 0:
    #                     break
    #             start = j
    #     else:
    #         if ladders[i][start+1] == 1:
    #             j = start + 1
    #             while ladders[i][j+1] == 1:
    #                 j += 1
    #                 if j == 99:
    #                     break
    #             start = j
    #         elif ladders[i][start-1] == 1:
    #             j = start - 1
    #             while ladders[i][j-1] == 1:
    #                 j -= 1
    #                 if j == 0:
    #                     break
    #             start = j

    print('#{} {}'.format(tc, start))