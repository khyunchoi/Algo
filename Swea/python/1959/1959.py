T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    
    max_result = 0
    for i in range(abs(M - N)+1):
        result = 0
        for j in range(min(M, N)):
            if N > M:
                result += A_list[i+j] * B_list[j]
            else:
                result += A_list[j] * B_list[i+j]
        
        max_result = max(max_result, result)
    
    print(f'#{tc} {max_result}')