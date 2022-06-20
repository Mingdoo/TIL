# TIL

## 1. NPM

> npm은 Node Package Manager의 약자로, Node.js로 만들어진 모듈을 웹에서 받아서 설치하고 관리해주는 프로그램이다. ( Java와 비교하면 메이븐과 비슷한 역할)

또한, 개발자가 업데이트를 할 경우 체크를 해서 알려준다. 즉, 버전 관리에 효율적인 package management라고 볼 수 있다.

- 사용 방법

npm을 설치한다.

[Node.js](https://nodejs.org/ko/)는 npm을 내장하고 있기 때문에, 따로 설치할 필요는 없다.

npm은 Node.js 위에서 모듈을 관리하기 때문에, npm을 사용한다는 것은 Node.js 생태계 위의 오픈소스나 라이브러리를 활용하여 구현한다는 것을 의미합니다. 즉, npm을 사용하는 이유는 모듈을 활용한다는 것입니다. 그러면 모듈을 다운로드 하기 위해서는 어떻게 해야할까요?

```bash
npm install -g [package_name]
```

정확히 구분하자면, `npm install`을 사용하는 방법은 접미어에 따라 구분됩니다.

1. 패키지명을 명시해 특정 패키지를 설치하는 동작
2. 패키지명을 명시하지 않고 `package.json` 파일의 의존성을 설치하는 동작

예를 들어,

```bash
npm install react
```

위와 같은 npm 명령어는 react라는 모듈을 설치하고 `package.json`에 버전 정보를 남기는 반면,

```bash
npm install
#혹은
npm i
```

이는 `package.json`에 포함된 의존성 패키지들이 일괄적으로 설치되는 방법입니다.

또한, 접미어(플래그)를 붙여 특정 패키지를 설치하는 방법도 있는데,

1. 프로젝트를 구동할 때 필요한 `dependencies` 목록에 추가될 패키지를 설치하는 경우

   ```bash
   npm install [package_name]
   ```

2. 개발 단계에서 필요한 `devDependencies` 목록에 추가될 옵션이 있습니다.

   ```bash
   npm install -D [package_name]
   ```

`-D`와 같은 접미어를 `플래그`라고 하는데, 주로 사용되는 플래그는 다음과 같습니다.

| flag        | effect                                                       |
| ----------- | ------------------------------------------------------------ |
| -P          | 패키지를 설치하고, 프로젝트의 `dependencies` 목록에 추가한다. |
| --save-prod | 패키지를 설치하고, 프로젝트의 `dependencies` 목록에 추가한다. |
| -D          | 패키지를 설치하고, 프로젝트의 `devDependencies` 목록에 추가한다. |
| --save-dev  | 패키지를 설치하고, 프로젝트의 `devDependencies` 목록에 추가한다. |
| -g          | 패키지를 프로젝트가 아닌 시스템의 `node_modules` 폴더에 설치한다. (global) |

- `-P`, `--save-prod`
  - default로서, `npm install [package_name]`과 동일하기 때문에 잘 사용되지 않는다.
- `-D`, `--save-dev`
  - 동일하게 프로젝트 내의 `node_modules`에 설치되지만, 패키지명을 `dependencies`가 아닌 `devDependencies`에 기록한다는 차이가 있습니다.
  - 그럼 `dependencies`와 `devDependencies`의 차이는 뭘까요?
    - `dependencies` : 실제 코드에도 포함되며 앱 구동을 위해 필요한 의존성 파일들
    - `devDependencies` : 실제 코드에 포함되지 않으며 개발 단계에만 필요한 의존성 파일들
- `-g`, `--global` 
  - `-g`를 사용하여 설치했을 경우, 시스템 폴더에 패키지를 설치하게 됩니다.
  - Win 10 기준으로는 `[username]\AppData\Roaming\npm\node_modules`
  - 시스템의 `node_modules` 폴더 경로는 `npm root -g`를 통해 찾을 수 있으며, `-g` 플래그를 사용할 경우 `package.json`에 기록되지 않습니다.

### 의존성 패키지를 설치할 때는?

pc를 자주 이동하여 사용하는 경우에는, A 컴퓨터에서 작업중인 내용을 그대로 받아 사용하고 싶지만, 가지고있는 node_modules의 차이로 실행되지 않는 경우가 빈번한데, 이는 gitignore에 `node_modules`가 작용되기 때문입니다. 이는, package.json만으로도 구별이 가능한데, A 컴퓨터에서 작업한 내용을 github에 upload한 후, 컴퓨터 B에서 이를 실행하려면 다음과 같은 명령어를 실행할 수 있습니다.

```bash
npm install
```

이는, 의존성 패키지를 설치하는 방법으로 이해할 수 있습니다. `package.json`에는 다음과 같은 의존성이 적혀있는데,

```json
{
    "devDependencies": {
        "A_module" : "^5.3.0"
    },
    "dependencies": {
        "B_module" : "^4.17.1"
    }
}
```

만약 이렇게 기록된 `package.json`이 있고, `npm install -P`를 실행한다면 프로젝트는 `devDependencies`는 무시하고 `dependencies`에 기록된 패키지만을 설치합니다.



## Yarn

npm과 같이 자바 스크립트 매니저이다.

[Yarn](https://github.com/yarnpkg/yarn)

#### Npm vs Yarn

1. Speed (performance)

npm은 필수 단계를 순차적으로 진행하는 경향이 있어 다음 패키지로 넘어가기 전에 각 패키지를 완전히 설치해야 한다는 점이 있다. 그러나 yarn은 동시에 여러 패키지를 설치할 수 있기 때문에 속도 면에서 크게 향상된다는 차이점이 **있었다.** 그렇지만 npm V6.10.1과 yarn V1.17.3으로 속도차이가 근소했으며, 이제는 **거의 차이가 없다.**

2. Security

npm은 의존 관계를 가지는 다른 패키지들이 즉시 포함되도록 한다. 이 점은 보안 문제에 있어 여러 취약점을 불러올 수 있다고 한다. 반면에 yarn은 yarn.lock이나 package.json 파일에 있는 것들만 설치를 한다. 이런 방식은 모든 디바이스에 같은 패키지를 설치하는 것을 보장하기에 디바이스마다 다른 버전을 설치해 발생할 수 있는 버그를 줄일 수 이다. 이 점은 yarn과 npm을 비교할 때 중요한 부분이며, 보안성을 따질 때는 yarn이 더 좋다.

