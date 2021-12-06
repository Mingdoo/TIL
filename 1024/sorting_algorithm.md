# Sorting Algorithm 😀

#### 목표 : 시간복잡도 Big O order를 구해보자.

0. ## Big O module

**운이 좋게도, sorting algorithm을 구현한 뒤 시간복잡도를 계산해주는 모듈이 있었다. 이름하야 `bigO`**.

```bash
#in bash
pip install big-O-calculator
```

더 정확한건 [big-O-calculator](https://pypi.org/project/big-O-calculator/)로 들어가 확인해보시길..

```python
#big_O.py
from bigO import BigO
def test(function):
    lib = BigO()
    return lib.test_all(function)
```

앞으로 이 big_O.py의 test function을 사용할 것이다.😃(개꿀..)

파이썬은 함수를 일급 객체로 다루기 때문에 이런 일이 다 있구나..👍

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

> 구현 : python
>
> 거품이 일렁일렁 하는 모습을 닮았다고 하여 bubble sort. 내가 거품이 되기 싫으면 이정도는 해야겠지?😁

### GIF로 이해하기!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/bubble-sort-001.gif)

#### 시간 복잡도

> Best : O(n^2)
>
> Average : O(n^2)
>
> Worst : O(n^2) 사실 upgrade버전이 있다고는 함. 아마도 이중 포인터를 사용하지 않을까?(~~라고 할뻔.~~)

#### 공간 복잡도

> O(n) // 배열 내에서 `swap`만 하므로 차치하는 크기는 n개입니다!

왜 다 같냐구요? `swap`을 할지 안 할지는 몰라도 일단 비교는 다 해야하니까! 정확히는 `(n-1)n / 2`번 만큼.

Bubble sort가 stable한 이유 : swap과정에서 같은 key값의 data가 swap되는 경우가 없기 때문.

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

>구현 : python
>
>내가 넣을 위치는 정해져있어. 너는 대답만 "해 줘" 느낌의 알고리즘. 결국엔 비교를 다 해야하기 때문에 worst, best 모두 O(n^2)일 것이다.

### GIF로 이해하기!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/selection-sort-001.gif)

#### 시간 복잡도

> Best : O(n^2)
>
>Average : O(n^2)
>
>Worst : O(n^2)

#### 공간 복잡도

> O(n) 이유는 위와 동일.

왜 시간복잡도가 다 같냐구요? ~~아까 말했잖아.~~

Selection sort가 unstable한 이유 : `[5, 3, 2, 5, 1]`을 정렬한다고 생각해보시라. 맨 처음의 5는 첫번째 `swap`이후 맨 뒤로 이동하여 `[1, 3, 2, 5, 5]`가 될 것이다.(stable하지 않음.)

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

> 구현 : python
>
> 원카드 할때 손에 들고있는 카드 정리할때 이렇게 하잖슴~

#### GIF로 이해하기!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/insertion-sort-001.gif)

#### 시간복잡도

> Best : O(n) Time (정렬이 되어있으면 매 선택마다 비교할 필요가 없이 그대로 나옴~)
>
> Average : O(n^2) Time
>
> Worst : O(n^2) Time

#### 공간복잡도

> O(n)

참고로, insertion sort는 best time complexity가 좋아서 tim sort(파이썬 내장 sort)에서 사용한다.



4. ## Quick Sort(unstable)

```python
from big_O import test
import sys
from random import randint

def quicksort(arr):
    '''
    Best : O(n) Time 모두 같은애일 때(pythonic한 quicksort이기 때문에 가능한 방법이라고 생각함.)
    Average : O(nlog(n)) Time
    Worst : O(nlog(n)) Time // 사실 O(n^2) 이다.
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

> 구현 : python
>
> `divide and conquer(분할 정복)`의 예시로 좋은 알고리즘. `master theorem(recipe 라고도 배웠음)`을 참고하면 빠르게 time complexity인 T(n)을 구할 수 있을 것이다.
>
> 참고 : [마스터 정리](https://ko.wikipedia.org/wiki/%EB%A7%88%EC%8A%A4%ED%84%B0_%EC%A0%95%EB%A6%AC)

#### GIF로 이해하기!

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/quick-sort-001.gif)

> #### 이해..되니..? 😅

#### 시간 복잡도(사진 참고)

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/quick-sort-002.png)

> Best : `O(nlog(n))` // arr 내의 pivot의 개수를 세어주는 `enhanced quicksort(파이썬 코드)`는 `O(n)`.
>
> Average : `O(nlog(n))`
>
> Worst : O(n^2) (내 생각엔 진짜 최악의 최악의 최악의 연속이라면 `O(n^2)`인 듯.)

![img](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/quick-sort-003.png)

이 performance를 향상시키기 위해, 코드에서는 random pivot 방법을 사용했음.

```python
pivot = arr[randint(0, len(arr) - 1)]
```

근데 정~~~말 운안좋게 pivot이 최솟값이나 최댓값만 걸린다면 위의 사진처럼 depth마다 정확히 반땡이 아니라 n-1개로 나눠지기 때문에 `O(n^2)`일 것이다.

#### 공간 복잡도

> O(n)

아참, 여기서 maximum depth error가 발생한다면..(python에서는 1000번)

```python
import sys
sys.setrecursionlimit(n) # n은 맘대로
```



Quick sort가 unstable인 이유

> 생각해보면 간단하다. pivot을 잡은 뒤에 어거지로 앞뒤로 끼워넣는 형태이니까.
>
> `[1, 1, 1, 2, 3, 4]` 라고 가정해보자. pivot을 array[0]으로 잡는 순간!! pivot을 기준으로 왼쪽에 1들이 몰려있을 것이다. 근데 걔들은 이미 unstable하지 않은가..? QED.

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

> 내가 직접 코드를 작성했을 때는 `O(n^2)`으로 나온다.. 😂
>
> 그래서! 코드를! 가져왔다! (알고리즘은 같음..)
>
> 구현 : python
>
> `divide and conquer` 방식으로 구현된 정렬 알고리즘. 일단 최대한 잘게 쪼갠 다음! 합치기!
>
> 참고 : Tim sort에 merge sort가 사용된다. insertion sort + merge sort = tim sort `?`

#### GIF로 이해하기!

![알고리즘 Merge Sort](https://media.vlpt.us/images/emily0_0/post/d35d6b3f-e7d9-44e7-934f-fb9856de69e2/merge-sort.gif)

> quick sort는 이해하기 힘들었지만.. 직관적이다.

#### 시간 복잡도

> Best : `O(nlog(n))` Time
>
> Average : `O(nlog(n))` Time
>
> Worst : `O(nlog(n))` Time

#### 공간 복잡도

> O(n)

merge sort가 stable한 이유:

> 자칫 잘못 코딩하면 unstable할 가능성이 있다. 이는 divide된 left와 right를 비교할 때, 같은 값이 나오면 어떤 값을 먼저 가져갈 것인지에 따라 stable, unstable이 나뉜다. 왼쪽 element를 먼저 가져갈 경우는 stable, 그렇지 않은 경우는 unstable이라는 거시야!😸

추가 : merge sort는 **순차적 비교**이므로, linked list의 정렬을 사용할 때 효율적이다.

만약 linked list를 quick sort로 정렬한다면?

> 성능이 좋지 않음. 왜? quick sort는 임의접근이기 때문이다! (linked list에서의 random access는 불가능하고, 순차 접근만 가능함(탐색에 O(n)))

`linked list`는 삽입, 삭제 연산에서 효율적이지만, 접근 연산에서는 비효율적이란 말씀. => 오버헤드가 발생



6. ## Heap Sort(unstable)

```python
from big_O import test

def heapify(arr, n, i):
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[parent] < arr[left]:
        parent = left
	
    #elif 아니다 조심!
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

> 구현 : python
>
> 반복: i는 length부터 1까지
>
> 1. max heap을 만들고
> 2. 뽑고(0번째와 i번째 swap)
> 3. heapify(n-i개의 원소만 갖고)
>
> 간단하지만 heap의 구조를 이해해야 한다.
>
> heapify : 자식에서 시작. 부모보다 자식이 크면 자식과 부모 `swap`(좀 말이 그렇긴 한데). 이후 그 위의 부모와 비교후 `swap`!
>
> unsorted를 heapify하려면 length // 2부터 0번째 index까지 heapify를 하면 된다. 왜? `subtree가 max heap이라는 것을 달고 시작하기 때문.

#### GIF로 이해하자!

![File:Heap sort example.gif - Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/f/fe/Heap_sort_example.gif)

> heapify의 과정부터 시작한다.

#### 시간 복잡도

> Best : `O(nlog(n)) Time`
>
> Average : `O(nlog(n)) Time`
>
> Worst : `O(nlog(n)) Time`

정확히는 

1. heap building `(O(n))`
2. 뽑고 heapify * n번 `(O(nlog(n)))`
3. `O(n) + O(nlog(n)) = O(nlog(n))`

#### 공간 복잡도

> O(n)

Heap sort가 unstable한 이유

> [속보] heapify가 stable을 보장하지 않기 때문.. 충격

추가 : left와 right중 큰 애를 가져간다 했지 자식이 크다고 쏙 바꿔버리면 큰일남.

```python
    #elif 아니다 조심!
    if right < n and arr[parent] < arr[right]:
        parent = right
```

heap구조의 특징(`?`)중 하나는 0번 index를 root index로 사용하며, 실제로 인덱스의 접근을 사용하지는 않는다는 점인데, 코드에서는 그렇게 구현하지는 않았음.



7. ## Radix Sort(음 빨라.. 근데 좀.. 싫어..)

> integer(positive)를 sorting하기에 생각보다 좋은 sorting이지만, 자릿수가 커짐에 따라 꽤나 running time의 차이가 있음
>
> 개인적인 생각으론 enhanced counting sort라고 봄.

```python
def countingSort(arr, digit):
    n = len(arr)
    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다.
    output = [0] * (n)
    count = [0] * (10)

    # digit, 자릿수에 맞는 count에 += 1을 한다.
    for i in range(0, n):
        index = int(arr[i] / digit)
        count[(index) % 10] += 1

    # count 배열을 수정해 digit으로 잡은 포지션을 설정한다.
    for i in range(1, 10):
        count[i] += count[i - 1]
    # 결과 배열, output을 설정한다. 설정된 count 배열에 맞는 부분에 arr원소를 담는다.
    i = n - 1
    while i >= 0:
        index = int(arr[i] / digit)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    # arr를 결과물에 다시 재할당한다.
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):
    '''
    시간복잡도 : O(nd) / d는 자리수
    '''
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다.
    maxValue = max(arr)
    # 자릿수마다 countingSorting을 시작한다.
    digit = 1
    while int(maxValue / digit) > 0:
        countingSort(arr, digit)
        digit *= 10

    return arr
```

> 자리수마다 정렬하는 방법. 예를 들어 `[123,231,312]`가 있으면, 일의자리 수 부터 비교해서 차근차근 올라간다는 알고리즘.

#### 시간 복잡도

> `O(dn) ` d는 자리수, n은 개수

#### 공간 복잡도

> `O(d + n)`

문자열도 정렬이 가능하다는 좋~은 장점이 있음.

근데, 부동소수점 나오면 빤쓰런 해버리는 정렬.



8. ## Counting Sort(stable? unstable?)

> 이건 뭐 stable인지.. unstable인지..

말은 쉽다.

1. 최댓값의 크기만큼 배열을 만든다
2. 전부다 개수를 세어준다
3. 순서대로 개수에 맞게 새로운 배열을 채워준다.

> 근데 자연수만 되는거 아님니까.. 해봐야 정수정도로 확장 가능할 것 같음.

```python
def counting_sort(arr):
    '''
    Best : O(n) Time
    Average : O(n) Time
    Worst : O(n) Time

    라고 나오지만....!!!!!!!
    실제로는 O(n+k) // k는 최댓값
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

#### GIF로 이해하기!

![Counting Sort GIF - Counting Sort - Discover &amp; Share GIFs](https://c.tenor.com/zswbYsLbYqEAAAAd/counting-sort.gif)

#### 시간 복잡도

> `O(n + k)`, k는 최댓값

#### 공간 복잡도

> `O(k)`