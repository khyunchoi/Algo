import sys

N = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(N)]

print(round(sum(num_list)/N))

num_list.sort()

print(num_list[N//2])

cnt_dict = {}
for num in num_list:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

max_cnt = 0
for value in cnt_dict.values():
    max_cnt = max(max_cnt, value)

max_num_list = []
for key, value in cnt_dict.items():
    if value == max_cnt:
        max_num_list.append(key)

max_num_list.sort()
if len(max_num_list) > 1:
    print(max_num_list[1])
else:
    print(max_num_list[0])

print(num_list[-1] - num_list[0])