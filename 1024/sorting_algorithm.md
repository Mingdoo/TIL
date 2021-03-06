# Sorting Algorithm ๐

#### ๋ชฉํ : ์๊ฐ๋ณต์ก๋ Big O order๋ฅผ ๊ตฌํด๋ณด์.

0. ## Big O module

**์ด์ด ์ข๊ฒ๋, sorting algorithm์ ๊ตฌํํ ๋ค ์๊ฐ๋ณต์ก๋๋ฅผ ๊ณ์ฐํด์ฃผ๋ ๋ชจ๋์ด ์์๋ค. ์ด๋ฆํ์ผ `bigO`**.

```bash
#in bash
pip install big-O-calculator
```

๋ ์ ํํ๊ฑด [big-O-calculator](https://pypi.org/project/big-O-calculator/)๋ก ๋ค์ด๊ฐ ํ์ธํด๋ณด์๊ธธ..

```python
#big_O.py
from bigO import BigO
def test(function):
    lib = BigO()
    return lib.test_all(function)
```

์์ผ๋ก ์ด big_O.py์ test function์ ์ฌ์ฉํ  ๊ฒ์ด๋ค.๐(๊ฐ๊ฟ..)

ํ์ด์ฌ์ ํจ์๋ฅผ ์ผ๊ธ ๊ฐ์ฒด๋ก ๋ค๋ฃจ๊ธฐ ๋๋ฌธ์ ์ด๋ฐ ์ผ์ด ๋ค ์๊ตฌ๋..๐

1. ## Bubble Sort(stable)

```python
from big_O import test

def bubble_sort(arr):
    '''
    Best : O(n^2) Time
    Average : O(n^2) Time
    Worst : O(n^2) Time
    '''
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

print(test(bubble_sort))
```

> ๊ตฌํ : python
>
> ๊ฑฐํ์ด ์ผ๋ ์ผ๋  ํ๋ ๋ชจ์ต์ ๋ฎ์๋ค๊ณ  ํ์ฌ bubble sort. ๋ด๊ฐ ๊ฑฐํ์ด ๋๊ธฐ ์ซ์ผ๋ฉด ์ด์ ๋๋ ํด์ผ๊ฒ ์ง?๐

### GIF๋ก ์ดํดํ๊ธฐ!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/bubble-sort-001.gif)

#### ์๊ฐ ๋ณต์ก๋

> Best : O(n^2)
>
> Average : O(n^2)
>
> Worst : O(n^2) ์ฌ์ค upgrade๋ฒ์ ์ด ์๋ค๊ณ ๋ ํจ. ์๋ง๋ ์ด์ค ํฌ์ธํฐ๋ฅผ ์ฌ์ฉํ์ง ์์๊น?(~~๋ผ๊ณ  ํ ๋ป.~~)

#### ๊ณต๊ฐ ๋ณต์ก๋

> O(n) // ๋ฐฐ์ด ๋ด์์ `swap`๋ง ํ๋ฏ๋ก ์ฐจ์นํ๋ ํฌ๊ธฐ๋ n๊ฐ์๋๋ค!

์ ๋ค ๊ฐ๋๊ตฌ์? `swap`์ ํ ์ง ์ ํ ์ง๋ ๋ชฐ๋ผ๋ ์ผ๋จ ๋น๊ต๋ ๋ค ํด์ผํ๋๊น! ์ ํํ๋ `(n-1)n / 2`๋ฒ ๋งํผ.

Bubble sort๊ฐ stableํ ์ด์  : swap๊ณผ์ ์์ ๊ฐ์ key๊ฐ์ data๊ฐ swap๋๋ ๊ฒฝ์ฐ๊ฐ ์๊ธฐ ๋๋ฌธ.

2. ## Selection Sort(unstable)

```python
from big_O import test

def selection_sort(arr):
    '''
    Best : O(n^2) Time
    Average : O(n^2) Time
    Worst : O(n^2) Time
    '''
    length = len(arr)
    for i in range(length):
        index = i
        for j in range(i+1, length):
            if arr[j] < arr[index]:
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return arr
```

>๊ตฌํ : python
>
>๋ด๊ฐ ๋ฃ์ ์์น๋ ์ ํด์ ธ์์ด. ๋๋ ๋๋ต๋ง "ํด ์ค" ๋๋์ ์๊ณ ๋ฆฌ์ฆ. ๊ฒฐ๊ตญ์ ๋น๊ต๋ฅผ ๋ค ํด์ผํ๊ธฐ ๋๋ฌธ์ worst, best ๋ชจ๋ O(n^2)์ผ ๊ฒ์ด๋ค.

### GIF๋ก ์ดํดํ๊ธฐ!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/selection-sort-001.gif)

#### ์๊ฐ ๋ณต์ก๋

> Best : O(n^2)
>
>Average : O(n^2)
>
>Worst : O(n^2)

#### ๊ณต๊ฐ ๋ณต์ก๋

> O(n) ์ด์ ๋ ์์ ๋์ผ.

์ ์๊ฐ๋ณต์ก๋๊ฐ ๋ค ๊ฐ๋๊ตฌ์? ~~์๊น ๋งํ์์.~~

Selection sort๊ฐ unstableํ ์ด์  : `[5, 3, 2, 5, 1]`์ ์ ๋ ฌํ๋ค๊ณ  ์๊ฐํด๋ณด์๋ผ. ๋งจ ์ฒ์์ 5๋ ์ฒซ๋ฒ์งธ `swap`์ดํ ๋งจ ๋ค๋ก ์ด๋ํ์ฌ `[1, 3, 2, 5, 5]`๊ฐ ๋  ๊ฒ์ด๋ค.(stableํ์ง ์์.)

3. ## Insertion Sort(stable)

```python
from big_O import test

def insertion_sort(arr):
    '''
    Best : O(n) Time
    Average : O(n^2) Time
    Worst : O(n^2) Time
    '''
    length = len(arr)
    for i in range(1, length):
        tmp = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > tmp:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = tmp
    return arr
```

> ๊ตฌํ : python
>
> ์์นด๋ ํ ๋ ์์ ๋ค๊ณ ์๋ ์นด๋ ์ ๋ฆฌํ ๋ ์ด๋ ๊ฒ ํ์์ด~

#### GIF๋ก ์ดํดํ๊ธฐ!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/insertion-sort-001.gif)

#### ์๊ฐ๋ณต์ก๋

> Best : O(n) Time (์ ๋ ฌ์ด ๋์ด์์ผ๋ฉด ๋งค ์ ํ๋ง๋ค ๋น๊ตํ  ํ์๊ฐ ์์ด ๊ทธ๋๋ก ๋์ด~)
>
> Average : O(n^2) Time
>
> Worst : O(n^2) Time

#### ๊ณต๊ฐ๋ณต์ก๋

> O(n)

์ฐธ๊ณ ๋ก, insertion sort๋ best time complexity๊ฐ ์ข์์ tim sort(ํ์ด์ฌ ๋ด์ฅ sort)์์ ์ฌ์ฉํ๋ค.



4. ## Quick Sort(unstable)

```python
from big_O import test
import sys
from random import randint

def quicksort(arr):
    '''
    Best : O(n) Time ๋ชจ๋ ๊ฐ์์ ์ผ ๋(pythonicํ quicksort์ด๊ธฐ ๋๋ฌธ์ ๊ฐ๋ฅํ ๋ฐฉ๋ฒ์ด๋ผ๊ณ  ์๊ฐํจ.)
    Average : O(nlog(n)) Time
    Worst : O(nlog(n)) Time // ์ฌ์ค O(n^2) ์ด๋ค.
    '''
    if len(arr) <= 1:
        return arr
    pivot = arr[randint(0, len(arr) - 1)]
    l = []
    eq = []
    r = []
    for e in arr:
        if e < pivot:
            l.append(e)
        elif e == pivot:
            eq.append(e)
        else:
            r.append(e)

    return quicksort(l) + eq + quicksort(r)
```

> ๊ตฌํ : python
>
> `divide and conquer(๋ถํ  ์ ๋ณต)`์ ์์๋ก ์ข์ ์๊ณ ๋ฆฌ์ฆ. `master theorem(recipe ๋ผ๊ณ ๋ ๋ฐฐ์ ์)`์ ์ฐธ๊ณ ํ๋ฉด ๋น ๋ฅด๊ฒ time complexity์ธ T(n)์ ๊ตฌํ  ์ ์์ ๊ฒ์ด๋ค.
>
> ์ฐธ๊ณ  : [๋ง์คํฐ ์ ๋ฆฌ](https://ko.wikipedia.org/wiki/%EB%A7%88%EC%8A%A4%ED%84%B0_%EC%A0%95%EB%A6%AC)

#### GIF๋ก ์ดํดํ๊ธฐ!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/quick-sort-001.gif)

> #### ์ดํด..๋๋..? ๐

#### ์๊ฐ ๋ณต์ก๋(์ฌ์ง ์ฐธ๊ณ )

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/quick-sort-002.png)

> Best : `O(nlog(n))` // arr ๋ด์ pivot์ ๊ฐ์๋ฅผ ์ธ์ด์ฃผ๋ `enhanced quicksort(ํ์ด์ฌ ์ฝ๋)`๋ `O(n)`.
>
> Average : `O(nlog(n))`
>
> Worst : O(n^2) (๋ด ์๊ฐ์ ์ง์ง ์ต์์ ์ต์์ ์ต์์ ์ฐ์์ด๋ผ๋ฉด `O(n^2)`์ธ ๋ฏ.)

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/quick-sort-003.png)

์ด performance๋ฅผ ํฅ์์ํค๊ธฐ ์ํด, ์ฝ๋์์๋ random pivot ๋ฐฉ๋ฒ์ ์ฌ์ฉํ์.

```python
pivot = arr[randint(0, len(arr) - 1)]
```

๊ทผ๋ฐ ์ ~~~๋ง ์ด์์ข๊ฒ pivot์ด ์ต์๊ฐ์ด๋ ์ต๋๊ฐ๋ง ๊ฑธ๋ฆฐ๋ค๋ฉด ์์ ์ฌ์ง์ฒ๋ผ depth๋ง๋ค ์ ํํ ๋ฐ๋ก์ด ์๋๋ผ n-1๊ฐ๋ก ๋๋ ์ง๊ธฐ ๋๋ฌธ์ `O(n^2)`์ผ ๊ฒ์ด๋ค.

#### ๊ณต๊ฐ ๋ณต์ก๋

> O(n)

์์ฐธ, ์ฌ๊ธฐ์ maximum depth error๊ฐ ๋ฐ์ํ๋ค๋ฉด..(python์์๋ 1000๋ฒ)

```python
import sys
sys.setrecursionlimit(n) # n์ ๋ง๋๋ก
```



Quick sort๊ฐ unstable์ธ ์ด์ 

> ์๊ฐํด๋ณด๋ฉด ๊ฐ๋จํ๋ค. pivot์ ์ก์ ๋ค์ ์ด๊ฑฐ์ง๋ก ์๋ค๋ก ๋ผ์๋ฃ๋ ํํ์ด๋๊น.
>
> `[1, 1, 1, 2, 3, 4]` ๋ผ๊ณ  ๊ฐ์ ํด๋ณด์. pivot์ array[0]์ผ๋ก ์ก๋ ์๊ฐ!! pivot์ ๊ธฐ์ค์ผ๋ก ์ผ์ชฝ์ 1๋ค์ด ๋ชฐ๋ ค์์ ๊ฒ์ด๋ค. ๊ทผ๋ฐ ๊ฑ๋ค์ ์ด๋ฏธ unstableํ์ง ์์๊ฐ..? QED.

5. ## Merge Sort(stable)

```python
from big_O import test

def merge_sort(arr):
    '''
    Best : O(nlog(n)) Time
    Average : O(nlog(n)) Time
    Worst : O(nlog(n)) Time
    '''
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

> ๋ด๊ฐ ์ง์  ์ฝ๋๋ฅผ ์์ฑํ์ ๋๋ `O(n^2)`์ผ๋ก ๋์จ๋ค.. ๐
>
> ๊ทธ๋์! ์ฝ๋๋ฅผ! ๊ฐ์ ธ์๋ค! (์๊ณ ๋ฆฌ์ฆ์ ๊ฐ์..)
>
> ๊ตฌํ : python
>
> `divide and conquer` ๋ฐฉ์์ผ๋ก ๊ตฌํ๋ ์ ๋ ฌ ์๊ณ ๋ฆฌ์ฆ. ์ผ๋จ ์ต๋ํ ์๊ฒ ์ชผ๊ฐ  ๋ค์! ํฉ์น๊ธฐ!
>
> ์ฐธ๊ณ  : Tim sort์ merge sort๊ฐ ์ฌ์ฉ๋๋ค. insertion sort + merge sort = tim sort `?`

#### GIF๋ก ์ดํดํ๊ธฐ!

![์๊ณ ๋ฆฌ์ฆ Merge Sort](https://media.vlpt.us/images/emily0_0/post/d35d6b3f-e7d9-44e7-934f-fb9856de69e2/merge-sort.gif)

> quick sort๋ ์ดํดํ๊ธฐ ํ๋ค์์ง๋ง.. ์ง๊ด์ ์ด๋ค.

#### ์๊ฐ ๋ณต์ก๋

> Best : `O(nlog(n))` Time
>
> Average : `O(nlog(n))` Time
>
> Worst : `O(nlog(n))` Time

#### ๊ณต๊ฐ ๋ณต์ก๋

> O(n)

merge sort๊ฐ stableํ ์ด์ :

> ์์นซ ์๋ชป ์ฝ๋ฉํ๋ฉด unstableํ  ๊ฐ๋ฅ์ฑ์ด ์๋ค. ์ด๋ divide๋ left์ right๋ฅผ ๋น๊ตํ  ๋, ๊ฐ์ ๊ฐ์ด ๋์ค๋ฉด ์ด๋ค ๊ฐ์ ๋จผ์  ๊ฐ์ ธ๊ฐ ๊ฒ์ธ์ง์ ๋ฐ๋ผ stable, unstable์ด ๋๋๋ค. ์ผ์ชฝ element๋ฅผ ๋จผ์  ๊ฐ์ ธ๊ฐ ๊ฒฝ์ฐ๋ stable, ๊ทธ๋ ์ง ์์ ๊ฒฝ์ฐ๋ unstable์ด๋ผ๋ ๊ฑฐ์์ผ!๐ธ

์ถ๊ฐ : merge sort๋ **์์ฐจ์  ๋น๊ต**์ด๋ฏ๋ก, linked list์ ์ ๋ ฌ์ ์ฌ์ฉํ  ๋ ํจ์จ์ ์ด๋ค.

๋ง์ฝ linked list๋ฅผ quick sort๋ก ์ ๋ ฌํ๋ค๋ฉด?

> ์ฑ๋ฅ์ด ์ข์ง ์์. ์? quick sort๋ ์์์ ๊ทผ์ด๊ธฐ ๋๋ฌธ์ด๋ค! (linked list์์์ random access๋ ๋ถ๊ฐ๋ฅํ๊ณ , ์์ฐจ ์ ๊ทผ๋ง ๊ฐ๋ฅํจ(ํ์์ O(n)))

`linked list`๋ ์ฝ์, ์ญ์  ์ฐ์ฐ์์ ํจ์จ์ ์ด์ง๋ง, ์ ๊ทผ ์ฐ์ฐ์์๋ ๋นํจ์จ์ ์ด๋ ๋ง์. => ์ค๋ฒํค๋๊ฐ ๋ฐ์



6. ## Heap Sort(unstable)

```python
from big_O import test

def heapify(arr, n, i):
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[parent] < arr[left]:
        parent = left
	
    #elif ์๋๋ค ์กฐ์ฌ!
    if right < n and arr[parent] < arr[right]:
        parent = right

    if i != parent:
        arr[parent], arr[i] = arr[i], arr[parent]
        heapify(arr, n, parent)

def heap_sort(arr):
    '''
    Best : O(nlog(n)) Time
    Average : O(nlog(n)) Time
    Worst : O(nlog(n)) Time
    '''
    length = len(arr)

    for i in range(length // 2, -1, -1):
        heapify(arr, length, i)

    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

print(test(heap_sort))
```

> ๊ตฌํ : python
>
> ๋ฐ๋ณต: i๋ length๋ถํฐ 1๊น์ง
>
> 1. max heap์ ๋ง๋ค๊ณ 
> 2. ๋ฝ๊ณ (0๋ฒ์งธ์ i๋ฒ์งธ swap)
> 3. heapify(n-i๊ฐ์ ์์๋ง ๊ฐ๊ณ )
>
> ๊ฐ๋จํ์ง๋ง heap์ ๊ตฌ์กฐ๋ฅผ ์ดํดํด์ผ ํ๋ค.
>
> heapify : ์์์์ ์์. ๋ถ๋ชจ๋ณด๋ค ์์์ด ํฌ๋ฉด ์์๊ณผ ๋ถ๋ชจ `swap`(์ข ๋ง์ด ๊ทธ๋ ๊ธด ํ๋ฐ). ์ดํ ๊ทธ ์์ ๋ถ๋ชจ์ ๋น๊ตํ `swap`!
>
> unsorted๋ฅผ heapifyํ๋ ค๋ฉด length // 2๋ถํฐ 0๋ฒ์งธ index๊น์ง heapify๋ฅผ ํ๋ฉด ๋๋ค. ์? `subtree๊ฐ max heap์ด๋ผ๋ ๊ฒ์ ๋ฌ๊ณ  ์์ํ๊ธฐ ๋๋ฌธ.

#### GIF๋ก ์ดํดํ์!

![File:Heap sort example.gif - Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/f/fe/Heap_sort_example.gif)

> heapify์ ๊ณผ์ ๋ถํฐ ์์ํ๋ค.

#### ์๊ฐ ๋ณต์ก๋

> Best : `O(nlog(n)) Time`
>
> Average : `O(nlog(n)) Time`
>
> Worst : `O(nlog(n)) Time`

์ ํํ๋ 

1. heap building `(O(n))`
2. ๋ฝ๊ณ  heapify * n๋ฒ `(O(nlog(n)))`
3. `O(n) + O(nlog(n)) = O(nlog(n))`

#### ๊ณต๊ฐ ๋ณต์ก๋

> O(n)

Heap sort๊ฐ unstableํ ์ด์ 

> [์๋ณด] heapify๊ฐ stable์ ๋ณด์ฅํ์ง ์๊ธฐ ๋๋ฌธ.. ์ถฉ๊ฒฉ

์ถ๊ฐ : left์ right์ค ํฐ ์ ๋ฅผ ๊ฐ์ ธ๊ฐ๋ค ํ์ง ์์์ด ํฌ๋ค๊ณ  ์ ๋ฐ๊ฟ๋ฒ๋ฆฌ๋ฉด ํฐ์ผ๋จ.

```python
    #elif ์๋๋ค ์กฐ์ฌ!
    if right < n and arr[parent] < arr[right]:
        parent = right
```

heap๊ตฌ์กฐ์ ํน์ง(`?`)์ค ํ๋๋ 0๋ฒ index๋ฅผ root index๋ก ์ฌ์ฉํ๋ฉฐ, ์ค์ ๋ก ์ธ๋ฑ์ค์ ์ ๊ทผ์ ์ฌ์ฉํ์ง๋ ์๋๋ค๋ ์ ์ธ๋ฐ, ์ฝ๋์์๋ ๊ทธ๋ ๊ฒ ๊ตฌํํ์ง๋ ์์์.



7. ## Radix Sort(์ ๋นจ๋ผ.. ๊ทผ๋ฐ ์ข.. ์ซ์ด..)

> integer(positive)๋ฅผ sortingํ๊ธฐ์ ์๊ฐ๋ณด๋ค ์ข์ sorting์ด์ง๋ง, ์๋ฆฟ์๊ฐ ์ปค์ง์ ๋ฐ๋ผ ๊ฝค๋ running time์ ์ฐจ์ด๊ฐ ์์
>
> ๊ฐ์ธ์ ์ธ ์๊ฐ์ผ๋ก  enhanced counting sort๋ผ๊ณ  ๋ด.

```python
def countingSort(arr, digit):
    n = len(arr)
    # ๋ฐฐ์ด์ ํฌ๊ธฐ์ ๋ง๋ output ๋ฐฐ์ด์ ์์ฑํ๊ณ  10๊ฐ์ 0์ ๊ฐ์ง count๋ ๋ฐฐ์ด์ ์์ฑํ๋ค.
    output = [0] * (n)
    count = [0] * (10)

    # digit, ์๋ฆฟ์์ ๋ง๋ count์ += 1์ ํ๋ค.
    for i in range(0, n):
        index = int(arr[i] / digit)
        count[(index) % 10] += 1

    # count ๋ฐฐ์ด์ ์์ ํด digit์ผ๋ก ์ก์ ํฌ์ง์์ ์ค์ ํ๋ค.
    for i in range(1, 10):
        count[i] += count[i - 1]
    # ๊ฒฐ๊ณผ ๋ฐฐ์ด, output์ ์ค์ ํ๋ค. ์ค์ ๋ count ๋ฐฐ์ด์ ๋ง๋ ๋ถ๋ถ์ arr์์๋ฅผ ๋ด๋๋ค.
    i = n - 1
    while i >= 0:
        index = int(arr[i] / digit)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    # arr๋ฅผ ๊ฒฐ๊ณผ๋ฌผ์ ๋ค์ ์ฌํ ๋นํ๋ค.
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):
    '''
    ์๊ฐ๋ณต์ก๋ : O(nd) / d๋ ์๋ฆฌ์
    '''
    # arr ๋ฐฐ์ด์ค์์ maxValue๋ฅผ ์ก์์ ์ด๋ digit, ์๋ฆฟ์๊น์ง ๋ฐ๋ณตํ๋ฉด ๋ ์ง๋ฅผ ์ ํ๋ค.
    maxValue = max(arr)
    # ์๋ฆฟ์๋ง๋ค countingSorting์ ์์ํ๋ค.
    digit = 1
    while int(maxValue / digit) > 0:
        countingSort(arr, digit)
        digit *= 10

    return arr
```

> ์๋ฆฌ์๋ง๋ค ์ ๋ ฌํ๋ ๋ฐฉ๋ฒ. ์๋ฅผ ๋ค์ด `[123,231,312]`๊ฐ ์์ผ๋ฉด, ์ผ์์๋ฆฌ ์ ๋ถํฐ ๋น๊ตํด์ ์ฐจ๊ทผ์ฐจ๊ทผ ์ฌ๋ผ๊ฐ๋ค๋ ์๊ณ ๋ฆฌ์ฆ.

#### ์๊ฐ ๋ณต์ก๋

> `O(dn) ` d๋ ์๋ฆฌ์, n์ ๊ฐ์

#### ๊ณต๊ฐ ๋ณต์ก๋

> `O(d + n)`

๋ฌธ์์ด๋ ์ ๋ ฌ์ด ๊ฐ๋ฅํ๋ค๋ ์ข~์ ์ฅ์ ์ด ์์.

๊ทผ๋ฐ, ๋ถ๋์์์  ๋์ค๋ฉด ๋นค์ฐ๋ฐ ํด๋ฒ๋ฆฌ๋ ์ ๋ ฌ.



8. ## Counting Sort(stable? unstable?)

> ์ด๊ฑด ๋ญ stable์ธ์ง.. unstable์ธ์ง..

๋ง์ ์ฝ๋ค.

1. ์ต๋๊ฐ์ ํฌ๊ธฐ๋งํผ ๋ฐฐ์ด์ ๋ง๋ ๋ค
2. ์ ๋ถ๋ค ๊ฐ์๋ฅผ ์ธ์ด์ค๋ค
3. ์์๋๋ก ๊ฐ์์ ๋ง๊ฒ ์๋ก์ด ๋ฐฐ์ด์ ์ฑ์์ค๋ค.

> ๊ทผ๋ฐ ์์ฐ์๋ง ๋๋๊ฑฐ ์๋๋๊น.. ํด๋ด์ผ ์ ์์ ๋๋ก ํ์ฅ ๊ฐ๋ฅํ  ๊ฒ ๊ฐ์.

```python
def counting_sort(arr):
    '''
    Best : O(n) Time
    Average : O(n) Time
    Worst : O(n) Time

    ๋ผ๊ณ  ๋์ค์ง๋ง....!!!!!!!
    ์ค์ ๋ก๋ O(n+k) // k๋ ์ต๋๊ฐ
    '''
    res = []
    mx = max(arr)
    count = [0] * (mx + 1)
    for e in arr:
        count[e] += 1

    for i in range(mx+1):
        if count[i]:
            for _ in range(count[i]):
                res.append(i)
    return res
```

#### GIF๋ก ์ดํดํ๊ธฐ!

![Counting Sort GIF - Counting Sort - Discover &amp; Share GIFs](https://c.tenor.com/zswbYsLbYqEAAAAd/counting-sort.gif)

#### ์๊ฐ ๋ณต์ก๋

> `O(n + k)`, k๋ ์ต๋๊ฐ

#### ๊ณต๊ฐ ๋ณต์ก๋

> `O(k)`