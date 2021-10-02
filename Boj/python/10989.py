import sys

N = int(input())

cnt_list = [0 for i in range(10001)]
for i in range(N):
    cnt_list[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if cnt_list[i]:
        for _ in range(cnt_list[i]):
            print(i)