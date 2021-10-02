N = int(input())
area = [[-1 for i in range(1001)] for j in range(1001)] 

paper_lists = []
for _ in range(N):
    paper_lists.append(list(map(int, input().split())))

total = [0 for i in range(N)]
for i in range(N):
    for j in range(paper_lists[i][0], paper_lists[i][0] + paper_lists[i][2]):
        for k in range(paper_lists[i][1], paper_lists[i][1] + paper_lists[i][3]):
            if area[j][k] != -1:
                total[area[j][k]] -= 1
            area[j][k] = i
            total[i] += 1

for i in range(N):
    print(total[i])