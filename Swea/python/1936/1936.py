A, B = map(int, input().split())

if A + B == 4:
    if A < B:
        print('A')
    else:
        print('B')
else:
    if A > B:
        print('A')
    else:
        print('B')