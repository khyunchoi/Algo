N = int(input())

xy_list = []
for _ in range(N):
    xy_list.append(list(map(int, input().split())))
xy_list.sort()

max_y = 0
for i in xy_list:
    if max_y < i[1]:
        max_y = i[1]

xy_list1 = []
xy_list2 = []
for i in range(len(xy_list)):
    if xy_list[i][1] == max_y:
        xy_list1 = xy_list[:i+1]
        break

for i in range(len(xy_list)-1, -1, -1):
    if xy_list[i][1] == max_y:
        xy_list2 = xy_list[i:]
        break
xy_list2.sort(reverse=True)

total1 = 0
x1, y1 = xy_list1[0][0], xy_list1[0][1]
for i in xy_list1:
    if i[1] > y1:
        total1 += (i[0] - x1) * y1
        x1 = i[0]
        y1 = i[1]

total2 = (xy_list2[-1][0] - xy_list1[-1][0] + 1) * max_y

total3 = 0
x2, y2 = xy_list2[0][0], xy_list2[0][1]
for i in xy_list2:
    if i[1] > y2:
        total3 += (x2 - i[0]) * y2
        x2 = i[0]
        y2 = i[1]

print(total1 + total2 + total3)