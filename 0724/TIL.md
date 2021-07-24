# Today I leared

##### 1. 달팽이 숫자 복습
```python
def snail():
    
    #주어진 Array와 현상태로 다음 state를 결정하는 것!
    def status(Arr, i, j, state):
        if state == 'right':
            if (j == len(Arr)-1):
                return 'down'
            elif Arr[i][j+1] != 0:
                return 'down'
            else:
                return 'right'
        if state == 'left':
            if i == 0:
                return 'up'
            elif Arr[i][j-1] != 0:
                return 'up'
            else:
                return 'left'
        if state == 'down':
            if i == len(Arr)-1:
                return 'left'
            elif Arr[i+1][j] != 0:
                return 'left'
            else:
                return 'down'
        if state == 'up':
            if Arr[i-1][j] != 0:
                return 'right'
            else:
                return 'up'
            
    rep = int(input())
    for _ in range(rep):
        N = int(input())
        #이 부분은 0723 TIL에서 배운 내용 (뒤에 if <condition>이 들어가도 됨)
        list_ = [[0 for x in range(N)] for y in range(N)]
        
        #초기조건
        number = 2
        i = j = 0
        state = 'right'
        list_[0][0] = 1
        
        while (number <= N**2):
        
            if state == 'right':
                j += 1
                list_[i][j] = number
                number += 1
                state = status(list_, i, j, state)
            elif state == 'left':
                j -= 1
                list_[i][j] = number
                number += 1
                state = status(list_, i, j, state)
        
            elif state == 'down':
                i += 1
                list_[i][j] = number
                number += 1
                state = status(list_, i, j, state)
            elif state == 'up':
                i -= 1
                list_[i][j] = number
                number += 1
                state = status(list_, i, j, state)
        print(f'#{_+1}')
        for row in list_:
            
            for elem in row:
                print(elem, end=' ')
            print()

snail()
```

