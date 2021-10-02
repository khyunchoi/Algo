for tc in range(10):
    N = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(N):
        boxes.sort()
        boxes[-1] -= 1
        boxes[0] += 1
    
        if N % 2:
            if max(boxes) - min(boxes) == 1:
                break
        else:
            if max(boxes) == min(boxes):
                break
    
    print(f'#{tc+1} {max(boxes) - min(boxes)}')