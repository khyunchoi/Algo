def factorial(num):
    if num < 2:
        return 1

    return num * factorial(num-1)


N = int(input())

print(factorial(N))