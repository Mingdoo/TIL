# TIL

## Babel & Webpack

### Webpack

> When webpack processes your application, it internally builds a `dependency graph` from one or more entry points and then combines every module your project needs into one or more bundles, which are static assets to serve your content from.

#### Core concepts;

- entry
  - An entry point indicates which module webpack should use to begin building out its internal `dependency graph`. webpack will figure out which other modules and libraries that entry point depends on.
- dependency graph
  - Any time one file depends on another, webpack treats this as a dependency.
- output
  - defaults to `./dist/main.js`.
- loaders
  - webpack only understands Javascript and JSON files. `Loader` allow webpack to process other type of files and convert them into valid modules.
- plugins
  - to transform certain types of modules, plugins can be leveraged to perform a wider range of tasks like bundle optimization
- mode
  - by using `mode` parameter to `development`, `production`, `none` enable webpack's built-in optimizations.

### 그래서 뭐가 좋은데?

#### 모듈 번들러

![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F997A63425B8AB8D923)

- 여러개의 파일을 하나로 묶어준다.
- 파일의 종속성을 스스로 파악하여, 서로 엮여있는 파일을 하나의 파일로 묶어주는 역할을 수행한다.

#### 네트워크 병목현상 해결

- 많은 자바스크립트를 로드할 경우, 네트워크에 병목현상이 발생하는데, 하나의 큰 파일을 로드하면 되는데, 하나의 자바스크립트로 개발하기엔 가독성과 유지보수 효율이 떨어지기 때문에, 이를 방지하기 위해 webpak을 사용한다.

#### 모듈 단위 개발 가능

- 모듈 단위의 개발을 하나의 자바스크립트로 종속을 해결해주기 때문에 좋다.
- 가독성과 유지보수 효율이 좋다.
- 스코프에 신경 쓰지 않고 개발이 가능하게 한다.

## IIFE

- 즉시 실행 함수 표현(Immediately Invoked Function Expression)

```javascript
(function () {
  statement;
});
```

#### 주의

- IIFE 내부의 변수는 외부 범위에서 접근이 불가능함.
