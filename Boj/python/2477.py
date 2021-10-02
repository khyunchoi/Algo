K = int(input())

value_list = []
for _ in range(6):
    key1, value1 = map(int, input().split())
    value_list.append(value1)

area_list = [value_list[0] * value_list[5]]
for i in range(5):
    area_list.append(value_list[i] * value_list[i+1])

area = sum(area_list) - max(area_list) * 2
print(area * K)