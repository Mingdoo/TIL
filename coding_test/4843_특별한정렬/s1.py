import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())

    arr = list(map(int, input().split()))
    res = []
    for i in range(10):
        for j in range(len(arr)-1, i, -1):
            #even
            if not i % 2:
                tmp = arr[j]
                if tmp > arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
            #odd
            else:
                tmp = arr[j]
                if tmp < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
    print('#{}'.format(test_case), end = ' ')
    for number in arr[:10]:
        print(number, end = ' ')
    print()
