# Today I learned



## 1. error 종류

###### SyntaxError : 잘못된 문법

- 보통 코딩을 할 VS Code, 파이참과 같은 IDE(통합개발환경)에서 개발을 하는데, 이러면 어느정도 문법을 자동으로 교정해주기 때문에 크게 걱정하지 않아도 된다. 그래도 뭐 콜론 같은 거 빼먹는 경우가 종종 있어서 막상 실행하면 `SyntaxError: unvalid syntax` 라는 에러 메시지를 흔히 마주할 수 있다.

###### NameError : 참조변수 없음

- 이건 예를 들면 코드에서 변수 a 를 출력하도록 했는데, 코드 상에서 a 를 선언한 적이 없다면 발생하는 에러다. `NameError: name 'a' is not defined` 라고 뜰 거다. 정의되지 않았다는 뜻이 되겠다.

###### ZeroDivisionError : 0으로 나눌 수 없음

- 파이썬에서 `print(10/0)`이라고 코딩을 해버리면, 10 나누기 0 값을 출력한다는 의미인데, 이건 문법적으로는 에러가 없지만 막상 실행하면 런타임 시에 `ZeroDivisionError: division by zero` 라는 오류 메시지가 뜬다. 엑셀에서도 숫자 좀 다뤄본 경험이 있다면 `#DIV/0!`를 본 적 있을 거다. 같은 거다.

###### IndexError : 인덱스 범위 벗어남

- 예를 들어 `a = [10, 20, 30] `이라는 원소 3개를 가진 리스트에서 `print(a[4])`와 같이 4번째 원소를 호출할 경우 발생하는 에러다. `IndexError: list index out of range` 라고 범위를 벗어났다는 메시지가 뜰 거다.

###### ValueError : 참조 값이 없음

- 예를 들어 `a = [10, 20, 30]` 이라는 원소 3개를 가진 리스트에서 `a.remove(40)`과 같이 40이라는 값을 가진 원소를 지우려고 하면 발생하는 애초에 그런 값이 없기 때문에 에러가 발생한다. `ValueError: list.remove(x): x not in list` 라고 그런 값이 리스트에 포함되어 있지 않다는 메시지가 뜬다. `a.index(40)`라고 써도 마찬가지겠지.

###### KeyError : 키 없음 에러 (주로 딕셔너리 사용시)

- `mydict = {'Kim': 1, 'Lee': 2}` 라는 딕셔너리가 있을 때 `print(mydict['Park'])`라고 출력하면 발생하는 에러다. `KeyError: 'Park'` 라고 메시지가 뜬다.

이럴 땐 get 메소드를 활용하면 좋다. `print(mydict.get('Park'))`라고 써보면 None이 출력된다. 키가 없을 경우 None값이 반환되기도 하고, 그 뒤에 키가 없을 때 반환할 값을 지정해놓아도 된다. 이렇게 `print(mydict.get('Park', 'unknown'))`

###### AttributeError : 모듈, 클래스의 잘못된 속성 사용함

- 예를 들어 `import time`으로 `time` 모듈을 활용하고자 할 때 time.sleep()이라고 하면 에러가 안 나지만, time.month()라고 엉뚱한 함수를 사용하면 에러가 발생한다. `AttributeError: module 'time' has no attribute 'month'`라고, time 모듈은 month라는 속성이 없다고 친절하게 알려준다. (물론 그 전에 IDE를 사용하면 에디터 상에서 알아서 내가 사용할 수 있는 속성들을 안내해주지만…)

###### FileNotFoundError : 파일 못 찾음

- 예를 들어 어떤 텍스트 파일을 읽기 위해 `f= open('ex.txt', 'r')`이라고 쳤을 때, 해당 경로에 파일이 없다면 `FileNotFoundError: [Errno 2] No such file or directory: 'ex.txt'` 라는 메시지가 뜬다. 그런 파일이나 디렉토리(폴더)가 없다는 뜻이다.

###### TypeError : 타입 안 맞음

- a = [1,2] 라고 리스트를 만들어 놓고, b = “Hello”라고 문자열을 만든 뒤 둘을 더하기로 연결해보자. print(a+b)라고 하면 `TypeError: can only concatenate list (not "str") to list` 라고 해서 리스트는 (문자열이 아닌) 리스트와 결합할 수 있습니다~ 라고 뜬다.



더 많은 error는 [python 공식문서](https://docs.python.org/ko/3/library/exceptions.html) 참고



## 2. 예외 처리 전략 (EAFP vs LBYL)

지금까지 살펴본 것들만 해도 종류가 참 많은데 또 어디서 어떤 에러가 발생할지 모른다. 그래서 예외를 처리하기 위해 크게 두가지 전략을 사용하곤 한다.

### EAFP

이건 **“It’s Easier to Ask Forgiveness than Permission”**, 미리 허락을 구하는 것보다는 나중에 용서를 구하는 게 쉽다는 뜻이다. 그래서 일단 항상 예외가 발생하지 않을 것으로 가정하고 나름대로의 완벽한 코딩을 한다. 그리고 막상 실행을 했는데 런타임 에러가 발생한다면 그때 예외처리 코딩을 하는 게 좋다는 철학이다. 그래서 일단 수행(try)시키고, 만약 에러가 발생하면 그때 처리(except)한다는 스타일로 코딩한다.

### LBYL

이건 **“Look Before You Leap”**, 누울 자리를 보고 다리를 뻗으라는 뜻. 어떤 코드를 실행하기 전에 에러가 발생할 수 있는 조건을 미리 다 따져보고 그걸 어떻게 처리할지 조건문(if) 스타일로 코딩한다.

> 참고로 파이썬에서는 LBYL보다 **EAFP**를 권장한다. ([PEP-0463](https://www.python.org/dev/peps/pep-0463/))



## 3. 파이썬 예외처리의 기본 try-except-else-finally

예외 처리는 이 네 개만 알면 된다.

- try : 에러 발생 가능성이 있는 코드 실행
- except : 에러 발생 시 (생략 가능, 여러개 사용 가능)
- else : 에러가 발생하지 않았을 경우 실행 (생략 가능)
- finally : 항상 실행 (생략 가능)

그리고 위에서 설명한 에러 종류들을 직접 명시해서 `except ValueError:` , `except NameError:` 이런 식으로 써도 되지만, 어떤 에러가 발생할지 모르겠을 때는 최종적으로 `except Exception:` 이라고 해서 이런저런 에러를 무조건 다 잡아버릴 수도 있다. `except Exception as e:` 라고 쓰고 `print(e)`로 출력하면 에러 내용을 확인할 수도 있다.



> 출처 : [아무튼 워라밸](http://hleecaster.com/python-exception/)



