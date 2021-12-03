import sys
from itertools import combinations

sys.stdin = open('input.txt')


def move(peoples, num, time, in_stair, visited):
    for people in peoples:
        if people[0] < stairs[num][0]:
            people[0] += 1
        elif people[0] > stairs[num][0]:
            people[0] -= 1
        else:
            if people[1] < stairs[num][1]:
                people[1] += 1
            elif people[1] > stairs[num][1]:
                people[1] -= 1
            else:
                if len(in_stair) < 3:
                    in_stair.append(0)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    peoples = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                peoples.append([i, j])
            elif 2 <= board[i][j] <= 10:
                stairs.append([i, j])
    
    combi_people = []
    for i in range(len(peoples) + 1):
        for combi in combinations(range(len(peoples)), i):
            combi_people.append(combi)
    
    result = float('inf')
    for combi in combi_people:
        stair_a = []
        stair_b = []
        for i in range(len(peoples)):
            if i in combi:
                stair_a.append(peoples[i])
            else:
                stair_b.append(peoples[i])
        
        move(stair_a, 0, 0, [])
        move(stair_b, 1, 0, [])