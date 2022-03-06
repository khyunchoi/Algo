def square(a, b):
    if b == 1:
        return a % C

    tmp = square(a, b // 2)

    if b % 2 == 1:
        return tmp * tmp * a % C
    else:
        return tmp * tmp % C


A, B, C = map(int, input().split())

print(square(A, B) % C)