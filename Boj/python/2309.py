height_list = []
for _ in range(9):
    height_list.append(int(input()))

target_sum = sum(height_list) - 100

for i in range(9):
    for j in range(i+1, 9):
        if height_list[i] + height_list[j] == target_sum:
            height_list.pop(i)
            height_list.pop(j-1)

            height_list.sort()

            for i in height_list:
                print(i)
            
            exit()