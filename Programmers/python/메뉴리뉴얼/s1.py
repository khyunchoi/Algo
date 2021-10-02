from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        combi_list = []
        for order in orders:
            tmp_list = list(map(list, combinations(order, i)))
            for tmp in tmp_list:
                tmp.sort()
                if tmp not in combi_list:
                    combi_list.append(tmp)

        max_cnt = 0
        result = []
        for combi in combi_list:
            cnt = 0
            for order in orders:
                for char in combi:
                    if char not in order:
                        break
                else:
                    cnt +=1
            if max_cnt < cnt:
                max_cnt = cnt
                result = [combi]
            elif max_cnt == cnt:
                result.append(combi)
        
        if max_cnt >=2:
            for arr in result:
                arr.sort()
                answer.append(''.join(arr))

    answer.sort()
    return answer
