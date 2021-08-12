import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    board = [[0] * 10 for _ in range(10)]
    rep = int(input())

    for _ in range(rep):
        information = list(map(int, input().split()))
        for i in range(information[1], information[3] + 1):
            for j in range(information[0], information[2] + 1):
                if not board[i][j] or board[i][j] == information[4]:
                    board[i][j] = information[4]
                else:
                    board[i][j] = '*'

    purple = 0
    for row in board:
        for elem in row:
            if elem == '*':
                purple += 1

    print('#{} {}'.format(test_case, purple))
