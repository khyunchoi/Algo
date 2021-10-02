T = int(input())
for tc in range(1, T+1):
    word = input()
    new_word = ''
    for i in range(len(word)-1, -1, -1):
        new_word += word[i]


    if word == new_word:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
