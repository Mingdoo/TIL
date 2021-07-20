## 코드 스타일

> 코드를 어떻게 작성할 것입니까?

- [PEP8](https://www.python.org/dev/peps/pep-0008/) : python에서 제공하는 스타일 가이드

- [Google Style Guide](https://google.github.io/styleguide/pyguide.html) : 구글에서 제공하는 스타일 가이드

크게 보면 같고 세부한 부분만 다르다. 기업, 오픈소스등에서 사용되는 스타일 가이드는 조금 다를 수 있다.



## 주석

> 주석을 표현할 때 어떻게 표현할 것입니까?

```python
def function():
    """
    이 부분에 들어가는 내용은 docstring으로 함수의 기능을 설명한다.
    """

function.__doc__ #로 호출할 수 있다.

# 일반적으로 (#) 을 사용해서 주석처리를 한다. 여러줄을 드래그해서 ctrl+/ 로 한번에 주석처리가 가능하다.
```



## 코드라인

> 코드는 1줄에 1문장(statement)!

- 그렇지 않은 방법으로 사용하는 방법은

```python
print('hello');print('a')
```

와 같이 세미콜론(;)을 이용하여 문장을 구분할 순 있으나 많이 사용되진 않을 것 같다.



## 변수와 식별자

> (=) 을 통해 값을 할당한다.

`type()` 로 변수에 할당된 값의 타입을 확인할 수 있다.

`id()`로 변수에 할당된 값의 id값을 얻어낸다. (메모리주소)

> 할당은 뭔데?

```python
x = y = 10
# 과 같은 방법으로 x,y에 값을 할당할 수 있다!
# 또한,
x , y = 1, 2
# 와 같은 방법으로도 할당할 수 있다.
## (1,2)라는 tuple을 만들어서 x, y에 정수값인 1, 2를 할당한다.
```

,또 x, y에 할당되어있는 값을 바꾸려면,

```python
x,y = y, x
#와 같은 방법으로 swap할 수 있다.
```



#### 식별자

`False`, `None`, `True` 와 같은 문자는 예약어라고 하며, 변수명으로 이와같은 예약어의 이름으로 할당할 수 없다.

할 수 있는 경우엔 에러가 생기기 때문에 하지 않는 것이 좋다!

- 예약어의 이름을 확인하는 방법

```python
import keyword
print(keyword.kwlist)
#로 예약어의 list를 확인할 수 있다.
```



- 내장함수나 모듈의 이름으로 만들면 안됨.
  - 더이상 동작하지 않을 수도 있음!



## 데이터 타입

- 숫자 - int

> 다른 언어와 달리 매우 큰 수를 나타낼 때 오버플로우가 발생가지 않는 장점이 있다.
>
> 이는 Arbitrary precision arithmetic(임의 정밀도 산술) 을 통해 고정메모리가 아닌 가용메모리를 사용함.



- 숫자 - float

> 정수가 아닌 모든 실수는 float 타입이다!

실수는 개수가 무한하기 때문에 컴퓨터가 이를 표현하기 위해 2진수로 숫자를 표현한다.

이 과정에서 floating point rounding error가 발생하여

```python
3.14 - 3.02 == 0.12
#는 False가 나오게 된다.
## 왜?
3.14 - 3.02 = 0.12000000001
#로 표현되기 때문.
```

이를 해결하기 위해 math 모듈의 isclose 메소드를 활용한다.

```python
import math
math.isclose(3.14-3.02, 0.12)
#결과는 Boolean값!
```



- 숫자 - complex

```python
a = 3 + 4j
# j는 허수부분을 의미한다.
# a.real과 a.imag로 실수부, 허수부를 나눈다.
```



- 문자열(String)

> 모든 문자열은 str 타입! ('),(")를 사용해 표기한다.

- - 이스케이프 시퀀스(escape sequence)

> \를 사용해 여러 문자를 조작한다.



### String Interpolation

> 1. '{} {}' .format(a,b)
> 2. f'{variable}' # f-string



```python
import datetime
today = datetime.datetime.now()
print(f'{today:%y}년 {today:%m}월 {today:%d}일')
#와 같은 방법으로 사용할 수 있다.
```



### Boolean

- True / False
- 비교 / 논리 연산에 사용

`0` , `0.0`, `()`, `[]`, `{}`, `''`, `None` 은 모두 False로 변환된다.

- `None` 은 값이 없음을 표현하기 위한 NoneType



## 자료형 변환/타입 변환 (conversion, casting)

- implicit 
  - 의도하지 않고, 파이썬에서 변환해줌
- Explicit
  - 사용자가 함수를 활용해 의도적으로 변환

> 암시적 타입 변환

```python
True + 3 == 4

3 + 5.0 == 8.0

3 + 4j + 5 == (8 + 4j)
```

`int()`, `str()`, `float()` 등으로 casting



### 비교 연산자

- `is` : 객체 아이덴티티(OOP)

- None과 비교할 때는 항상 `is`를 사용.

```python
x = 3
print(x is None)
```



### 논리 연산자

- A `and ` B
- A `or` B
- `Not` A



## 컨테이너

> 여러개의 값을 저장할 수 있는 객체

- 시퀀스형 : ordered data
  - 순서가 있다 != 정렬되어 있다.
  - list, tuple, range, string, binary
- 비 시퀀스형 : unordered data
  - set

### list

- index를 통해 접근

```python
My_list = [1,2,3,4]
print(My_list[0])
```



### tuple

- 수정이 불가능한 타입(Immutable)

```python
My_tuple = (1,2,3,4)
```



### range

- 레인지는 숫자의 시퀀스를 나타내기 위해 사용
  - range(int n,int m,int s) : n이상 m미만 s만큼 증가시키며 사용



### set

- unordered data의 일종이다.

```python
My_set = set({1,2,3,3,4})
# {1,2,3,4}로 바뀜 => 집합과 성질이 같음
len(set(My_list))
# 로 list type을 set type으로 바꿀 수 있음!
```



### dictionary

- key와 value로 이루어진 자료구조

```python
dict_a = {}
#중괄호로만 만들어도 가능하다.
```



### 1 tab = 4 spaces in python

