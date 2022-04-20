# React Native cli vs Expo

### 누가 더 좋을까?

`React Native`는 개발의 상당 부분을 최고의 `Javascript` 라이브러리인 `React`를 사용합니다. 반면에, `Expo`는 `React Native` 위에 구축되었는데, 이 둘이 동일하다고 볼 수도 있습니다. 둘 다 `React Native`를 사용하지만 차이점이 존재합니다. 바로 **빌드 방법**입니다.

React Native는 궁극적으로는 `Javascript bridging`에 의해 `Java`코드로 변환됩니다. Native module은 항상 javascript 코드보다 빠른데, 모듈을 장착할 때에 React Native CLI를 사용하면 쉽게 구현이 가능하지만, Expo를 사용할 때는 그렇지 않은 경우가 많습니다. 또, Expo CLI를 사용하는 경우는 대개 사출하는 단계에서 expo 모듈에 의존하게 되는 문제가 존재합니다.

빌드 프로세스에서도 차이가 존재하는데, `Expo`는 모든 프로젝트 빌드를 `Expo Cloud`위에서 수행하는 반면, `React Native`는 사용자의 시스템에서 수행합니다. 즉, Gradle 실패나 매니페스트 오류 등의 빌드 오류를 직접 해결해야 하는데, `Expo`는 그렇지 않습니다.

#### 퍼포먼스

`Expo App`과 `React Native App`은 빌드 시에 용량의 차이가 큽니다. 이는 번들의 포함때문인 것으로 보입니다.

### 결론

두 CLI 모두 React Native, ReactJS, Javascript에 대한 선수 지식이 충분히 필요함은 분명합니다. 다만, iOS 빌드용 Mac이 있는 경우 RN-CLI를 사용하는 것이 App bundle을 빌드할 때 용량을 최소화할 수 있습니다.



#### 

