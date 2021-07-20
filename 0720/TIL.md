Today I learned

> 210720 today I learned!



##### 1. zip() method

```python
'''
To use this method, we need more than 2 lists.
for example, for list a and b, we make them each tuple by elementwise.
'''

a = [
    'a',
    'b',
]
b = [
    1,
    2,
]

zipper = zip(a,b)
dic = dict(zipper)

print(dic)
```

**result** :

```python
{'seoul': '02', 'gg': '031'}
# we can make it list, tuple or dictionary type.
```



##### 2. get method for dictionary type

```python
location = {'seoul': '02', 'gg': '031'}

#if we use get(key) method for dictionary type, such as
location.get('seoul')
```

**result** : '02'

```python
#otherwise, if there is no keys that we put in, for example,
location.get('SSAFY')
#returns None
```



##### 3. ''' ''' code line

```python
'''
주석
'''

"""
이렇게도 사용 가능
"""

print("""
by PEP-8, print multiple line by '""" """'.
""")
```



##### 4. expression for octal number, hexadecimal number, binary number

```python
octal_number = 0o10
hexadecimal_number = 0x10
binary_number = 0b10
```



##### 5. String interpolation

```python
# %-formatting
name = 'Minsu'
print('%s' %name)

#f-string and str.format()
print('{}'.format(name))
print(f'{name}')
```



##### 6. error for typecasting

```python
int('3.5') # not working
int(3.5) # working
int(float('3.5')) #working
```



##### 7.  short circuit evaluation(단축평가)

```python
print(0 and 3) #do not check 3 for boolean value. why?
print(3 or 0) #do not check 0 for boolean value. why?
# 결과가 확정된 경우 뒤에 있는 경우를 확인하지 않는다.

#example)
print(3 or 4)
# => 3
print(4 or 3)
# => 4
```



##### 8. concatenation

```python
'a' + 'b' == 'ab'

[1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]
```



##### 9. identity

```python
#-5~256의 integer값의 id는 동일하다.
a = 255
b = 255
print(id(a))
print(id(b))
print(a is b)

#그러나, 소수점이 붙으면 다르다.
a = 255.2
b = 255.2
print(id(a))
print(id(b))
print(a is b)
```



##### 10. 연산자 우선순위

1. `()`을 통한 grouping

2. Slicing

3. Indexing

4. 제곱연산자
    `**`

4. 단항연산자 
    `+`, `-` (음수/양수 부호)

5. 산술연산자
    `*`, `/`, `%`
    
6. 산술연산자
    `+`, `-`

7. 비교연산자, `in`, `is`

8. `not`

9. `and` 

10. `or`



##### 11. 시퀀스에서 활용할 수 있는 연산자/함수

| operation    | 설명             |
| ------------ | ---------------- |
| x `in` s     | containment test |
| x `not in` s | containment test |
| s1 `+` s2    | concatenation    |
|s `*` n|n번만큼 반복하여 더하기|
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|



##### 12. Typora 표 만들기

```
|이름|이름|이름|
|-|-|-|
|ㅁㄴㅇ|ㅁㄴㅇ|ㅁㄴㅇ|
```



##### 13. pythontutor

- [pythontutor](http://pythontutor.com/)

- for문의 진행에 따라 가시적으로 보여주는 툴



##### 14. Mutable & Immutable Data

- Mutable
  - List
  - Dict
  - Set
- Immutable
  - Literal
    - 숫자(number)
    - 글자(string)
    - 참/거짓(bool)
  - <u>**Range**</u>
  - Tuple
  - Frozenset()



