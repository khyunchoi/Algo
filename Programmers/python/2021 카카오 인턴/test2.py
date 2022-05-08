def solution(places):
    def dfs(i, j, depth, trace):
        if depth == 1 and trace == 'P':
            result.append(0)
            return

        if depth == 2:
            if trace == 'OP':
                result.append(0)
            return

        for di, dj in dij:
            ni = i + di
            nj = j + dj

            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj] and place[ni][nj] != 'X':
                dfs(ni, nj, depth+1, trace+place[ni][nj])

    answer = []
    dij = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for place in places:
        result = []
        visited = [[0 for _ in range(5)] for _ in range(5)]

        for i in range(5):
            for j in range(5):
                if len(result) == 0 and place[i][j] == 'P':
                    visited[i][j] = 1
                    dfs(i, j, 0, '')

        if len(result) == 0:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))