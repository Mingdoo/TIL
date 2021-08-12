# 2001_파리퇴치

2차원 배열의 slicing하는 방법.
```python
board = [list(map(int, input().split())) for _ in range(N)]
# board의 선언(2차원)

specific_board = [row[j : j + M] for row in board[i : i + M]
#내가 뽑은 board.

#순서상 내가 원하는 board[i : i + M]을 먼저 뽑고, 그 row들을 대상으로 원하는 column값으로 슬라이싱하여 새로운 array에 append되는 방법.
```

- 실제로 사용한 코드는 다음과 같다.
```python
tmp = [sum(x) for x in [row[j : j + M] for row in board[i : i + M]]]
```
- 코드가 매우 지저분하여 역겹기 짝이 없다고 생각이 됨. 2차원이 아닌 다차원 list는 얼마나 기분나쁘게 생겼을까.