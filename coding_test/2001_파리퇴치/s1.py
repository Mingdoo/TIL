import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    N, M = list(map(int, input().split()))

    board = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0
    tmp = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 귀찮지만 list comprehension을 사용했다. 이차원 리스트 슬라이싱 어케하누 ㅠ.ㅠ
            tmp = [sum(x) for x in [row[j : j + M] for row in board[i : i + M]]]

            #아래 코드는 수정할 필요가 있긴 하지만 안 해도 그닥..
            tmp = sum(tmp)

            #일반적인 비교
            if tmp > maximum:
                maximum = tmp

    print('#{} {}'.format(test_case, maximum))



