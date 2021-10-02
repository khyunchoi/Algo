N = int(input())
paper = set()

for tc in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper.add((i, j))

print(len(paper))