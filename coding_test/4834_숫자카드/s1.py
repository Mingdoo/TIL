import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):

    num = int(input())
    inp = input()
    res = [0] * 10

    for char in inp:
        res[int(char)] += 1

    count = 0
    max_idx = 0
    for idx in range(10):
        if res[idx] >= count:
            count = res[idx]
            if idx >= max_idx:
                max_idx = idx

    print('#{} {} {}'.format(test_case, max_idx, count))