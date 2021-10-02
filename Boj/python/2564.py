width, height = map(int, input().split())
N = int(input())
store_list = []

for _ in range(N+1):
    news, num = map(int, input().split())
    if news == 1:
        store_list.append((num, 0))
    elif news == 2:
        store_list.append((num, height))
    elif news == 3:
        store_list.append((0, num))
    else:
        store_list.append((width, num))

donggun = store_list.pop()

total = 0
for store in store_list:
    if abs(store[0] - donggun[0]) == width:
        tmp_total = store[1] + donggun[1] + width
        if tmp_total > height + width:
            tmp_total = 2 * (height + width) - tmp_total

        total += tmp_total
    elif abs(store[1] - donggun[1]) == height:
        tmp_total = store[0] + donggun[0] + height
        if tmp_total > height + width:
            tmp_total = 2 * (height + width) - tmp_total

        total += tmp_total
    else:
        tmp_total = abs(store[0] - donggun[0]) + abs(store[1] - donggun[1])

        total += tmp_total

print(total)