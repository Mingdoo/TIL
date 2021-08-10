import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):

    number = int(input())
    height = list(map(int, input().split()))

    for i in range(number):
        #최고 높이가 여러개인 것은 중요하지 않다.
        #왜냐면 한번씩 하니까!
        max_idx = height.index(max(height))
        min_idx = height.index(min(height))

        height[max_idx] -= 1
        height[min_idx] += 1
    print('#{} {}'.format(test_case, max(height) - min(height)))