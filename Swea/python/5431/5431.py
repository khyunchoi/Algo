T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    checks = list(map(int, input().split()))
    students = [i for i in range(1, N+1)]

    for check in checks:
        students.remove(check)
    result = ' '.join(map(str, students))
    print(f'#{tc+1} {result}')