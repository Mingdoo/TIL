from copy import deepcopy
import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):

    Q_num = int(input())

    matrix = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        tmp = i

        X = i
        Y = 0

        #엄청난 if문의 하드코딩 인척?하는 알고리즘.
        #deepcopy로 지나온 길을 지우면서 가는게 더 편하다. 안 그러면
        #지금 어디로 가고있는지도 알려줘야 하기 때문.
        copy_matrix = deepcopy(matrix)
        while Y <= 98 and copy_matrix[Y][X] != 0:
            if X + 1 <= 99 and copy_matrix[Y][X + 1] == 1:
                copy_matrix[Y][X] = 0
                X += 1
            elif X - 1 >= 0 and copy_matrix[Y][X - 1] == 1:
                copy_matrix[Y][X] = 0
                X -= 1
            else:
                Y += 1
        if matrix[Y][X] == 2:
            res = tmp
            break
        #러닝타임이 생각보다 길다. 뭐가 잘못된걸까
    print('#{} {}'.format(Q_num, res))