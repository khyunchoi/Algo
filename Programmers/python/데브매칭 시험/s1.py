def solution(drum):
    answer = len(drum)
    for j in range(len(drum)):
        i = 0
        flag = 1
        while i < len(drum):
            if drum[i][j] == '#':
                i += 1
            elif drum[i][j] == '>':
                j += 1
            elif drum[i][j] == '<':
                j -= 1
            else:
                if flag:
                    flag = 0
                    i += 1
                else:
                    answer -= 1
                    break

    return answer





print(solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"]))