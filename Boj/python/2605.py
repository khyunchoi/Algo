N = int(input())
pick_list = list(map(int, input().split()))
students = []

for i in range(N):
    students.insert(i-pick_list[i], i+1)

print(' '.join(map(str, students)))