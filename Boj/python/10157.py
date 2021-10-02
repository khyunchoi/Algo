C, R = map(int, input().split())
K = int(input())

cnt = -1
init_C = C
init_R = R
init_K = K
while C > 0 and R > 0:
    K -= R
    cnt += 1
    if K <= 0:
        break
    R -= 1

    C -= 1
    K -= C
    cnt += 1
    if K <= 0:
        break

move = cnt // 4
if init_K > init_C * init_R:
    print(0)
else:    
    if cnt % 4 == 0:
        print(1 + move, init_R - move + K)
    elif cnt % 4 == 1:
        print(init_C - move + K, init_R - move)
    elif cnt % 4 == 2:
        print(init_C - move, 1 + move - K)
    else:
        print(2 + move - K, 1 + move)