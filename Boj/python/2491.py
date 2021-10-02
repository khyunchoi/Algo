N = int(input())
num_list = list(map(int, input().split()))

max_cnt = 1
cnt_bigger = 1
cnt_lower = 1
for i in range(N-1):
    if num_list[i] < num_list[i+1]:
        max_cnt = max(max_cnt, cnt_lower)
        cnt_lower = 1
        cnt_bigger += 1
    elif num_list[i] > num_list[i+1]:
        max_cnt = max(max_cnt, cnt_bigger)
        cnt_bigger = 1
        cnt_lower += 1
    else:
        cnt_bigger += 1
        cnt_lower += 1

    max_cnt = max(max_cnt, max(cnt_bigger, cnt_lower))

print(max_cnt)

# max_num = 0
# for i in range(N-1):
#     a, b = i, i
#     cnt_bigger = 1
#     while num_list[a] <= num_list[a+1]:
#         cnt_bigger += 1
#         a += 1
#         if a == N-1:
#             break
    
#     cnt_smaller = 1
#     while num_list[b] >= num_list[b+1]:
#         cnt_smaller += 1
#         b += 1
#         if b == N-1:
#             break
#     max_num = max(max(cnt_smaller, cnt_bigger), max_num)

# print(max_num)