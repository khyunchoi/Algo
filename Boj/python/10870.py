def fibo(i):
    if i < 2:
        return i

    return fibo(i-1) + fibo(i-2)


n = int(input())
print(fibo(n))