T = int(input())

for tc in range(T):
    N = int(input())
    init_N = N
    num_list = []

    while True:
        for i in str(N):
            if i not in num_list:
                num_list.append(i)
        
        if len(num_list) == 10:
            break
        N += init_N
    
    print(f'#{tc+1} {N}')