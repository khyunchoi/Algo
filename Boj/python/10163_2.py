N = int(input())
area = [[True for i in range(1001)] for j in range(1001)] 

paper_lists = []
for _ in range(N):
    paper_lists.append(list(map(int, input().split())))

cnt = 0
total = [0 for i in range(N)]
for i in range(N-1, -1, -1):
    for j in range(paper_lists[i][0], paper_lists[i][0] + paper_lists[i][2]):
        for k in range(paper_lists[i][1], paper_lists[i][1] + paper_lists[i][3]):
            if area[j][k]:
                area[j][k] = False
                total[i] += 1
                cnt += 1
            if cnt == 1001 * 1001:
                for l in range(N):
                    print(total[l])
                exit()

for i in range(N):
    print(total[i])