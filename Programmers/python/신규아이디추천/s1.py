def solution(new_id):
    # 1
    new_id_1 = new_id.lower()
    # 2
    new_id_2 = ''
    for char in new_id_1:
        if char.isalpha() or char.isdigit() or char in '-_.':
            new_id_2 += char
    # 3
    new_id_3 = ''
    i = 0
    while i < len(new_id_2):
        if i < len(new_id_2)-1 and new_id_2[i] == '.':
            new_id_3 += new_id_2[i]
            i += 1
            while new_id_2[i] == '.':
                if i == len(new_id_2)-1:
                    i += 1
                    break
                i += 1
        else:
            new_id_3 += new_id_2[i]
            i += 1
    # 4
    new_id_4 = new_id_3
    if len(new_id_4) and new_id_4[-1] == '.':
        new_id_4 = new_id_4[:-1]
    if len(new_id_4) and new_id_4[0] == '.':
        new_id_4 = new_id_4[1:]
    # 5
    if len(new_id_4) == 0:
        new_id_4 = 'a'
    # 6
    if len(new_id_4) > 15:
        new_id_4 = new_id_4[:15]
        if new_id_4[-1] =='.':
            new_id_4 = new_id_4[:-1]
    # 7
    while len(new_id_4) < 3:
        new_id_4 += new_id_4[-1]
    

    return new_id_4
