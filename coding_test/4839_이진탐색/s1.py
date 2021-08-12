import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    P, A, B = list(map(int, input().split()))

    start_A = start_B =  1
    end_A = end_B = P
    count_A = count_B = 0

    while start_A <= end_A:
        mid = int((start_A + end_A) / 2)
        count_A += 1
        if mid == A:
            break
        elif mid < A:
            start_A = mid
        else:
            end_A = mid

    while start_B <= end_B:
        mid = int((start_B + end_B) / 2)
        count_B += 1
        if mid == B:
            break
        elif mid < B:
            start_B = mid
        else:
            end_B = mid

    winner = 0
    if count_A < count_B:
        winner = 'A'
    elif count_A > count_B:
        winner = 'B'

    print('#{} {}'.format(test_case, winner))