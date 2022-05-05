def solution(s):
    answer = 0
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for key, value in num_dict.items():
        while key in s:
            s = s[:s.index(key)] + str(value) + s[s.index(key)+len(key):]

    answer = int(s)

    return answer



print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))