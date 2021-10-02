N = int(input())

init_N = N #초기화용 N
arr = []
max_num = 0
max_arr = []
for i in range(N//2, N+1):
    N = init_N
    arr = [N]

    while i >= 0:
        arr.append(i)
        N, i = i, N - i
    
    if len(arr) > max_num:
        max_num = len(arr)
        max_arr = arr

print(max_num)
for i in max_arr:
    print(i, end=' ')