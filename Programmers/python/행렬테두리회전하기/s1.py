def solution(rows, columns, queries):
    answer = []
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    tmp = 0
    for i in range(rows):
        for j in range(columns):
            tmp += 1
            board[i][j] = tmp
    
    for query in queries:
        r1, c1, r2, c2 = query
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

        result = float('inf')

        r, c = r1, c1
        tmp_num = board[r][c]
        while c < c2:
            c += 1
            result = min(result, tmp_num)
            board[r][c], tmp_num = tmp_num, board[r][c]

        while r < r2:
            r += 1
            result = min(result, tmp_num)
            board[r][c], tmp_num = tmp_num, board[r][c]

        while c > c1:
            c -= 1
            result = min(result, tmp_num)
            board[r][c], tmp_num = tmp_num, board[r][c]

        while r > r1:
            r -= 1
            result = min(result, tmp_num)
            board[r][c], tmp_num = tmp_num, board[r][c]

        answer.append(result)

    return answer

print(solution(100, 97, [[1, 1, 100, 97]]))