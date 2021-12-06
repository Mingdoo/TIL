# Today I learned



##### 1. 파이썬 패키지 만들기

- 패키지(package) : 패키지는 **점(`.`)으로 구분된 모듈 이름(`package.module`)** 을 써서 모듈을 구조화하는 방법을 말한다.

- python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식합니다(PEP 420). 하지만 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 `__init__.py` 파일을 생성하는 것이 권장된다.

  ###### [연습] 패키지 만들기

###### [폴더구조]
```python
my_package/
    __init__.py
    math/
        __init__.py
        tools.py  
    statistics/
        __init__.py
        tools.py
```

###### `standard_deviation()` 함수
```python
import math


def standard_deviation(values):
    mean = sum(values) / len(values)
    sum_var = sum(pow(value - mean, 2) for value in values) / len(values)
    std_dev = math.sqrt(sum_var)
    return std_dev
```

업로드 : [pypi에 패키지 업로드하기](https://wikidocs.net/78954)



##### 2.  Generic function In python with Singledispatch

```python
from functools import singledispatch


@singledispatch
# decorator!
def fprint(data):
    print(f'({type(data).__name__}) {data}')
    
#결과는 : 
#fprint
@fprint.register(list)
@fprint.register(set)
@fprint.register(tuple)

#fprint.register(list) ..
#와 같은 방법으로 decorate하는 것이 가능해졌다.
#Java에서 가능한 generic func가 가능하넹..;ㅋㅋ!!
def _(data):
    formatted_header = f'{type(data).__name__} -> index : value'
    print(formatted_header)
    print('-' * len(formatted_header))
    for index, value in enumerate(data):
        print(f'{index} : ({type(value).__name__}) {value}')
```



