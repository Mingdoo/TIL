import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    N, K = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]

    word_afford = []

    #전에 했던 row합, column합 응용이다. 쭉 더하다 0나오면 스탑

    #row
    for i in range(N):
        afford = 0
        for j in range(N):
            if board[i][j] != 0:
                afford += 1
                if j == N - 1:
                    word_afford.append(afford)
            else:
                if afford != 0:
                    word_afford.append(afford)
                afford = 0

    #column
    for i in range(N):
        afford = 0
        for j in range(N):
            if board[j][i] != 0:
                afford += 1
                if j == N - 1:
                    word_afford.append(afford)
            else:
                if afford != 0:
                    word_afford.append(afford)
                afford = 0

    count = 0

    #단순비교
    for number in word_afford:
        if K == number:
            count += 1
    print('#{} {}'.format(test_case, count))