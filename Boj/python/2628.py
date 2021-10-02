width, height = map(int, input().split())
N = int(input())

width_list = [0, width]
height_list = [0, height]
for _ in range(N):
    a, num = map(int, input().split())
    if a:
        width_list.append(num)
    else:
        height_list.append(num)

width_list.sort()
height_list.sort()

max_width = 0
for i in range(len(width_list) - 1):
    if max_width < width_list[i+1] - width_list[i]:
        max_width = width_list[i+1] - width_list[i]

max_height = 0
for i in range(len(height_list) - 1):
    if max_height < height_list[i+1] - height_list[i]:
        max_height = height_list[i+1] - height_list[i]

print(max_width * max_height)