T = int(input())

for tc in range(T):
    total = 0
    numbers = input()
    numbers_list = list(map(int, numbers.split()))
    
    for num in numbers_list:
        if num % 2:
            total += num
            
    print(f'#{tc+1} {total}')