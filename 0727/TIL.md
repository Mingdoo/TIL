# Today I learned



##### 1. `dict.get()` 메소드를 사용한 counting

우리는 큰 데이터를 다룰 때, 어떤 데이터가 얼마나 중복되어있는가 혹은 중복되어 있는 데이터가 얼마나 많이 중복 되어 있는가를 확인하고 싶어 할 것이다. 이 때, 이를 dictionary로 return할 수 있는 좋은 방법이 있다.

이는 `dict.get()`메소드를 사용하는 것인데, 이 메소드는 원하는 `key`값을 입력하고, 그 값이 dictionary에 없다면 default값을 return하고, 다른 값을 default로 입력한다면 그 값을 반환한다.

이 예시는 주어진 list데이터가 얼마나 중복되어있는 지를 dict 타입으로 반환하는 함수이다.

```python
def counting(arr):
    my_dict = {}
    for element in arr:
        #my_dict[element]를 my_dict.get의 디폴트값을 통해 접근하는 방법.
        my_dict[element] = my_dict.get(element, 0) + 1
    return my_dict
```

