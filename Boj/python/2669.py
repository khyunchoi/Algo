my_set = set()

for tc in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            my_set.add((i, j))

print(len(my_set))