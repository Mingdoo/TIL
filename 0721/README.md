# Today I learned



##### 1.

파이썬에서 함수는 어떻게 사용될까? 함수를 정의하고 호출하는 것은 맞는데, 실제로 그 과정이 어떻게 진행될까?

- [python stack](https://towardsdatascience.com/python-stack-frames-and-tail-call-optimization-4d0ea55b0542)

파이썬에서는 함수를 사용할 때, stack을 쌓아서 LIFO 방법으로 이를 호출한다.

```python
int(input())
```

이와 같은 코드를 실행할 때,

| )      |
| ------ |
| )      |
| input( |
| int(   |

위와 같은 방법으로 stack을 만들어 실행한다.



##### 2. 가변 인자 리스트, 가변 키워드 인자

함수의 input에 여러 값이 들어가야 한다면 어떻게 이를 정의하고 사용할 수 있을까?

- [가변 인자, 가변 키워드 인자](https://wikidocs.net/84426)

```python
#가변 인자 리스트
def add(*args):
    for arg in args:
        print(arg)

#가변 키워드 인자
def family(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
        
family(father='john', mother='jane')
```



##### 3. LEGB Rule

변수를 사용할 때 어떤 순서로 이를 불러올까?

- local scope : 함수
- enclosed scope : 특정 함수의 상위 함수
- global scope : 함수 밖의 변수
- built-in scope : 내장함수

[참고문서](https://realpython.com/python-scope-legb-rule/)



##### 4. nonlocal

global은 아니고.. 가장 가까운 변수에 접근하여 이를 수정하고 사용할 순 없을까?

- use `nonlocal`!

```python
x = 0
def fun1():
    x = 1
    print(x)
    def fun2():
        nonlocal x
        x = 3
    fun2()
    print(x)
fun1()
print(x)

#결과 : 1 3 0
```

#####  

##### 5. SyntaxError : positional arguments follows keyword argument

```python
def repeat_str_KeyArg_first(repeat_num, *strings):
   ...: result = [repeat_num * strings]
   ...: return result

repeat_str_KeyArg_first(repeat_num = 3, 'a', 'b', 'c') # SyntaxError
```

출처: [R, Python 분석과 프로그래밍의 친구 (by R Friend)](https://rfriend.tistory.com/465)

