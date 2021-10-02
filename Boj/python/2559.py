N, K = map(int, input().split())
temperature_list = list(map(int, input().split()))

part_sum = sum(temperature_list[:K])
max_part_sum = part_sum
for i in range(1, N - K + 1):   
    part_sum = part_sum - temperature_list[i-1] + temperature_list[i-1+K]
    
    if max_part_sum < part_sum:
        max_part_sum = part_sum
    
print(max_part_sum)