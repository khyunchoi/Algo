N = int(input())
arr = list(map(int, input().split()))
arr_tmp = list(set(arr))
result = []
dict_tmp = dict()

arr_tmp.sort()

tmp = 0
for num in arr_tmp:
    dict_tmp[num] = tmp
    tmp += 1

for num in arr:
    result.append(dict_tmp[num])

print(*result)