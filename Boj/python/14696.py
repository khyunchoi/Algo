N = int(input())

for tc in range(N):
    A_list = list(map(int, input().split()))
    A = A_list.pop(0)
    B_list = list(map(int, input().split()))
    B = B_list.pop(0)
    
    if A_list.count(4) > B_list.count(4):
        print('A')
        continue
    elif A_list.count(4) < B_list.count(4):
        print('B')
        continue
    else:
        if A_list.count(3) > B_list.count(3):
            print('A')
            continue
        elif A_list.count(3) < B_list.count(3):
            print('B')
            continue
        else:
            if A_list.count(2) > B_list.count(2):
                print('A')
                continue
            elif A_list.count(2) < B_list.count(2):
                print('B')
                continue
            else:
                if A_list.count(1) > B_list.count(1):
                    print('A')
                    continue
                elif A_list.count(1) < B_list.count(1):
                    print('B')
                    continue
                else:
                    print('D')
                    continue