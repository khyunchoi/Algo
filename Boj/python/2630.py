def paper(row, col, size):
    tmp = arr[row][col]
    flag = 0

    if size == 1:
        if tmp == 0:
            result[0] += 1
        else:
            result[1] += 1
        return

    for i in range(row, row+size):
        for j in range(col, col+size):
            if arr[i][j] != tmp:
                flag = 1
                break
        if flag:
            break
    
    if flag:
        paper(row, col, size//2)
        paper(row + size//2, col, size//2)
        paper(row, col + size//2, size//2)
        paper(row + size//2, col + size//2, size//2)
    else:
        if tmp == 0:
            result[0] += 1
        else:
            result[1] += 1
        return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]

paper(0, 0, N)

print(result[0])
print(result[1])