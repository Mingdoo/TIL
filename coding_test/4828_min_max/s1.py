import sys
sys.stdin = open('sample_input.txt', r)

T = int(input()) # T 문제에서 주어진 대로 사용


for test_case in range(1, T + 1): #직관적으로 보기 편함.
    N = int(input()) #문제에서 주어진 대로 사용

    max = -100000000
    min = 100000000

    given = list(map(int, input().split()))

    for element in given:
        max = element if element > max else max
        min = element if element < min else min

    print('#{0} {1}'.format(test_case, max - min)) #3.5 초과버전부터 f-string 가능