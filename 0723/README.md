# Today I learned



##### 1. `os.listdir()` 메소드

**<u>모르고 있던 점</u>** : os 모듈로 디렉토리 내의 모든 파일을 list형태로 뽑아올 수 있다는 것.

```python
json_files = 
[my_file for my_file in os.listdir('<directory>') if my_file.endswith('.<endname>')]

#문법.
[<name> for <name> in <iterable> if <condition>] #여기서 if condition은 빠져도 됨.

#os.listdir
os.listdir('path') => list(str)
```











---

##### 
