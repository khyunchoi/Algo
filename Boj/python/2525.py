hour, min = map(int, input().split())
tmp = int(input())

min += tmp

if (min // 60) >= 1:
    hour += min // 60
    min %= 60

if hour >= 24:
    hour %= 24

print(hour, min)
