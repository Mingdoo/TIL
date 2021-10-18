# TIL

##### 자연어 처리(nlp)



## 1. 단어 토큰화

- 단어를 기준으로 토큰화 하는것을 의미한다.

예를 들어, 

입력 : **Time is an illusion. Lunchtime double so!**

이라면, 출력은

출력 : "Time", "is", "an", "illustion", "Lunchtime", "double", "so"

와 같은 형식으로 나오는 것을 단어 토큰화라고 한다.

- 선택의 순간

토큰화를 하면, `don't`와 같은 어퍼스트로피(`'`)를 기준으로 어떻게 단어를 토큰화 해야 하는지가 애매해진다. 여기서,  `nltk.tokenize`의 `word_tokenize`는 다음과 같은 토큰화를 해낸다.

```python
from nltk.tokenize import word_tokenize  
print(word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
# ['Do', "n't", 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', ',', 'Mr.', 'Jone', "'s", 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop', '.']  
```

이는 Don't를 Do, n't로 분리하였음을 알 수 있다. 또, `WordPunctTokenizer`는 다음과 같이 단어를 토큰화한다.

```python
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
# ['Don', "'", 't', 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', ',', 'Mr', '.', 'Jone', "'", 's', 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop', '.'] 
```

이는 Don't를 Don, ' 그리고 t로 토큰화함을 알 수 있다. 이러한 선택의 순간에서 우리는 어떤 선택을 해야 할까?



- 표준 토큰화

표준 토큰화는 `Penn Treebank Tokenization`을 사용하는데, 이는 2가지 규칙을 가지고있다.

1. 하이픈으로 구성된 단어는 하나의 단어로 유지한다.

2. don't와 같은 접어가 함께한 단어는 분리해준다.

```python
from nltk.tokenize import TreebankWordTokenizer
tokenizer=TreebankWordTokenizer()
text="Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(text))
# ['Starting', 'a', 'home-based', 'restaurant', 'may', 'be', 'an', 'ideal.', 'it', 'does', "n't", 'have', 'a', 'food', 'chain', 'or', 'restaurant', 'of', 'their', 'own', '.'] 
```

결과는 Don't를 Do와 n't로 구별하였음을 알 수 있다.



## 2. 문장 토큰화

- 문장 단위로 토큰화 하는것을 의미한다.

코퍼스가 정제되지 않은 상태라고 가정했을 때, 일반적으로 `.`을 기준으로 문장을 구별하고 싶을 것이다. 그러나, `.(온점)`은 항상 문장의 마침을 나타내는 기호가 아니기 때문에 여러 문제를 야기한다.

입력 : **IP 192.168.56.31 서버에 들어가서 로그 파일 저장해서 ukairia777@gmail.com로 결과 좀 보내줘. 그러고나서 점심 먹으러 가자.**

결국 코퍼스가 어떤 언어인지, 특수문자가 어떻게 사용되고 있는지를 판별하여 직접 규칙을 정의할 수 있을 것이다. 여기서, 영어 문장의 토큰화를 도와주는 sent_tokenize를 사용하려고 한다.

```python
from nltk.tokenize import sent_tokenize
text="Enter the IP 192.168.56.31 server, save the log file, and send the results to ukairia777@gmail.com. Then let's go eat lunch."
print(sent_tokenize(text))
# ['Enter the IP 192.168.56.31 server, save the log file, and send the results to ukairia777@gmail.com.', "Then let's go eat lunch."]
```

컴퓨터의 IP같은 단어를 제대로 문장단위로 토큰화 하였음을 알 수 있다.

한국어의 특성을 포함하여 문장 토큰화를 개발한 `KSS(Korean Sentence Splitter)`가 있다.

```python
import kss
text='딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어려워요. 농담아니에요. 이제 해보면 알걸요?'
print(kss.split_sentences(text))
```

