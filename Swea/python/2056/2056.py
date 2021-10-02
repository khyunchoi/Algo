T = int(input())

for tc in range(T):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    result = f'{year}/{month}/{day}'

    year = int(year)
    month = int(month)
    day = int(day)
    

    if 1 <= month <= 12:
        if month == 2:
            if day > 28 or day <1:
                result = -1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30 or day <1:
                result = -1
        else:
            if day > 31 or day <1:
                result = -1
    else:
        result = -1

    print(f'#{tc+1} {result}')