import sys
sys.stdin = open('input.txt')

T = int(input())

arr = [i for i in range(1, 13)]
subset = [[]]

for number in arr:
    tmp = subset[:]
    for element in tmp:
        subset.append(element + [number])

for test_case in range(1, T + 1):

    N, K = list(map(int, input().split()))

    count = 0
    for s in subset:
        if len(s) == N and sum(s) == K:
            count += 1

    print('#{} {}'.format(test_case, count))