# Today I learned

> 210720 today I learned!



###### 1. zip() method

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

result :

```python
{'seoul': '02', 'gg': '031'}
# we can make it list, tuple or dictionary type.
```

