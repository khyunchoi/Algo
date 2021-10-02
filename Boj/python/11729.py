def hanoi(N, start, end, other):
    if N == 1:
        print(start, end)
        return

    hanoi(N-1, start, other, end)
    hanoi(1, start, end, other)
    hanoi(N-1, other, end, start)


N = int(input())
print(2**N - 1)
hanoi(N, 1, 3, 2)