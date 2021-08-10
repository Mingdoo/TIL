import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):

    K, N, M = list(map(int, input().split()))

    current = 0
    count = 0

    stop = list(map(int, input().split()))

    while current <= N:
        tmp = current

        if current + K >= N:
            break

        for step in range(K, 0, -1):
            if (current + step) in stop:
                current += step
                count += 1
                break
        if tmp == current:
            if current + K >= N:
                break
            else:
                count = 0
                break
    print('#{} {}'.format(test_case, count))
