### 개발 초기 설정(FE)

- expo 다운로드

  - ```bash
    npm install --global expo-cli
    ```

  - ```bash
    #프로젝트 디렉토리
    expo login
    #ID와 PW는 Notion에 있음
    ```

- 모바일 환경에서 expo go 다운로드

  - [Android](https://play.google.com/store/apps/details?id=host.exp.exponent)
  - [ios](https://apps.apple.com/kr/app/expo-go/id982107779)

- react native app(skeleton codes)

  - ```bash
    #at console(bash)
    expo init [projectName]
    
    # after initialization
    cd [projectName]
    npm start
    ```

  - 스켈레톤 코드는 Gitlab에 업데이트 할 예정입니다.

- 버전 컨트롤

  - node : v16.13.1

  - expo : v5.3.1

  - android : v8.0.0

  - ios : v15.2 (iphone 11)

- Extensions(vscode)

  - prettier (세미콜론 자동 생성)
  - expo tools


#### 추가 사항

`expo cli`와 `react native cli`중 expo를 고른 이유

- expo cli에서 제공하는 기능이 생각보다 좋다. virtual machine 기능 또한 제공하며, 사용중인 핸드폰이 build된 pc와 같은 네트워크에 있다면 물리적인 연결 없이 테스트할 수 있는 환경을 제공한다.
- object-C, swift를 사용할 필요가 없다. (expo는 이들을 지원하지 않음.)
- ios와 android 동시에 개발 가능한 장점이 있다.

`react native`의 장점

- react와 유사하게 구현하며, 컴파일 단계에서 andriod, ios 운영체제로 가는 bridge가 있어 javascript만으로 구현이 가능하다.



#### 참고 자료

[Ant Design for react native](https://rn.mobile.ant.design/docs/react/introduce)

[React native elements](https://reactnativeelements.com/)

[React native paper](https://callstack.github.io/react-native-paper/)

[Nativebase](https://nativebase.io/)
