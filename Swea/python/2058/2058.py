N = int(input())

total = 0
while N > 0:
    total += N % 10
    N = N //10

print(total)