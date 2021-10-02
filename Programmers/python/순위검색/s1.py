def solution(info, query):
    answer = []
    for sentence in query:
        cnt = 0
        tmp_list = list(sentence.split())
        for _ in range(3):
            tmp_list.remove('and')
        cnt_list = [0] * len(info)

        for i in range(len(tmp_list)-1):
            for j in range(len(info)):
                if cnt_list[j] == i and (tmp_list[i] == '-' or tmp_list[i] in info[j]):
                    cnt_list[j] += 1
        print(cnt_list)
        for i in range(len(cnt_list)):
            if cnt_list[i] == 4 and int(list(info[i].split())[4]) >= int(tmp_list[4]):
                cnt += 1
        
        answer.append(cnt)

    return answer



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))