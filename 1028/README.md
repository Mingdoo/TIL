# JS

자바스크립트 입문

## Variables

`var`, `let`, `const`는 다른 선언형태이다.

```javascript
const phone = 'Galaxy S2'
phone = 'asd' // error!!!!! const는 재할당이 불가능함
```

```javascript
let ssafy
ssafy = '제주도'
ssafy = '화성' // 얘는 재할당 가능
```

```javascript
var framework = 'Bootstrap'
framework = 'Django' // 재할당 가능
var framework = 'Vue' // 재선언 가능
```

- 함수 스코프

```javascript
function f1() {
  var message = 'You are doing great!'
}
console.log(message) // ReferenceError: message is not defined
```

- 블록 스코프

```javascript
const codeEditor = 'vscode'
if (codeEditor === 'vscode') {
  var theme = 'dark+' // var는 되지만 const, let은 블록 스코프에 걸림
}
console.log(theme) // 'dark+'
```

```javascript
function f2() {
  const stack = 'Last In, First Out'
}
console.log(stack) // ReferenceError: stack is not defined

function f3() {
  let queue = 'First In, First Out'
}
console.log(queue) // ReferenceError: queue is not defined
```

- 호이스팅

```javascript
console.log(hoisted) // undefined
var hoisted = 'can you see me?'

console.log(lunch) // ReferenceError: Cannot access 'lunch' before initialization
const lunch = '초밥'

console.log(dinner) // ReferenceError: dinner is not defined
let dinner = '스테이크'
```

## Conditions

- if

```javascript
const username = 'managersdas'
if (username === 'admin'){
  console.log('hi admin')
}
else if (username === 'manager'){
  console.log('hi manager')
}
else{
  console.log('hi', username)
}
```
if문에서 `===`는 Strict, 즉 엄격한 Equal Operator로써, "엄격하게" 같음을 비교할 때 사용하는 연산자이다. 

`===`는 a `===` b 라고 할때, 값과 값의 종류(Data Type)가 모두 같은지를 비교해서, 같으면 true, 다르면 false라고 한다.

- switch

```javascript
const operator = '+'
const a = 10
const b = 20

switch (operator){
  case '+':
    console.log(a+b)
    break
  case '-':
    console.log(a-b)
    break
  case '/':
    console.log(a/b)
    break
  case '*':
    console.log(a*b)
    break
  default:
    console.log('invalid')
}
```

- for ... in / for ... of

> for ...in // 객체 순환
> for ...of // 배열 값 순환



## Array Helper Methods

- map : 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환합니다.
- filter : 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환합니다.
- find : 주어진 판별 함수를 만족하는 **첫 번째 요소**의 **값**을 반환합니다. 그런 요소가 없다면 `undefined`를 반환합니다.
- every : 배열 안의 모든 요소가 주어진 판별 함수를 통과하는지 테스트합니다. Boolean 값을 반환합니다.
- some : 배열 안의 어떤 요소라도 주어진 판별 함수를 통과하는지 테스트합니다.
- reduce : 배열의 각 요소에 대해 주어진 **리듀서**(reducer) 함수를 실행하고, 하나의 결과값을 반환합니다.



## Functions

```javascript
function celsiusToFahrenheit (celsius) {
		const fahrenheit = celsius * 9/5 + 32
		return fahrenheit
}
//이렇게도 쓸 수 있음(화살표 함수)
const pow = x => x * x
```



## Arrays

```javascript
/*
	[배열 관련 주요 메서드 연습 2]
	주어진 배열을 사용하여 아래 문자열을 완성하세요.
	'www.samsung.com/sec/buds/galaxy-buds-pro'
*/
const arr1 = ['www', 'samsung', 'com']
const arr2 = ['galaxy', 'buds', 'pro']
const arr3 = ['sec', 'buds']
const result = arr1.join('.') + '/' + arr3.join('/') + '/' + arr2.join('-')
```

```javascript
/*
	[배열 관련 주요 메서드 연습 3]
	주어진 배열의 요소 중 모든 'rainy' 요소를 'sunny'로 교체하세요
	- indexOf 메서드를 사용합니다.
*/
const weather = ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'sunny']

while (weather.indexOf('rainy') >= 0) {
	weather[weather.indexOf('rainy')] = 'sunny'
}
```



## Objects

```javascript
/*
[Object 축약 문법]
아래 변수들을 속성으로 가지는 Object를 축약문법을 활용하여 작성하세요.
*/
const username = 'hailey'
const contact = '010-1234-5678'
const obj = {
  username,
  contact,
}
```



