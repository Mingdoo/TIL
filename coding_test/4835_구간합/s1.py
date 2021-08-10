import sys
sys.stdin = open('sample_input.txt')

repeat = int(input())

for i in range(repeat):
    N, M = list(map(int, input().split()))

    arr = list(map(int, input().split()))
    max = -1000000000
    min = 1000000000
    for idx in range(N - M + 1):
        if (sum(arr[idx: idx + M])) >= max:
            max = sum(arr[idx: idx + M])
        if (sum(arr[idx: idx + M])) <= min:
            min = sum(arr[idx: idx + M])
    print('#{} {}'.format(i + 1, max - min))