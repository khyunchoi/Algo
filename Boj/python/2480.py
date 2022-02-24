a, b, c = map(int, input().split())

result = 0
if a == b == c:
    result = 10000 + a * 1000
elif a == b or c == a:
    result = 1000 + 100 * a
elif b == c:
    result = 1000 + 100 * b
else:
    result = max(a, b, c) * 100

print(result)