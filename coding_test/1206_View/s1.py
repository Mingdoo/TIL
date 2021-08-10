import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    #총 건물의 개수 : number
    number = int(input())
    height = list(map(int, input().split()))


    count = 0

    for i in range(2, number - 2):
        #좌우 건물중 가장 높은 건물의 높이
        max_between_four_buildings = max(height[i-2 : i] + height[i+1 : i+3])
        if height[i] - max_between_four_buildings >= 1:
            count += height[i] - max_between_four_buildings


    print('#{} {}'.format(test_case, count))
