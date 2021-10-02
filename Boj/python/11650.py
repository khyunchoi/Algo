import sys

N = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.sort(key=lambda x : (x[0], x[1]))

for i in arr:
    print(*i)