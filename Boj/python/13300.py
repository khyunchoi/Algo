N, K = map(int, input().split())

students = {}
for _ in range(N):
    S, Y = map(int, input().split())
    if (S, Y) not in students:
        students[(S, Y)] = 1
    else:
        students[(S, Y)] += 1

total = 0
for student in students:
    total += (students[student] + K - 1) // K

print(total)