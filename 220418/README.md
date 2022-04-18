# Redux Core

### One way data flow

- resolves multiple component issue
- Lifting state
- extract shared state from component tree

### Terminology

- action {type, payload}
- reducer (state, action) => newState
- store (state lives) created by reducer
- dispatch is the only way to update state(pass in an action object)
- selectors is the function that extract specific pieces of information from a store state

### Initial setup

- store created by using reducer function
- store calls root reducer once to save initial state
- UI first rendered

### Updates

- Something happened === dispatch actions
- store run reducer with previous state with current action to save new state
- notifies all parts store has been updated / Each UI check update
- need to changed UI re-render

## Redux

for what?

- shared state
- flux structure
- store / reducer / action / selector



## Ducks pattern

기존에는 redux를 통한 상태관리의 파일 구조를 reducer, action, saga로 나누어 관리하는데, ducks패턴은 구조중심이 아닌 기능 중심으로 파일을 나눈다.

즉, action type, action 생성자 함수, saga, reducer를 하나의 파일에서 관리한다.

ducks패턴에서 각각의 action/function/reducer를 모아 module이라 한다.

이 때, 지켜야 할 점이 있다.

1. reducer는 export default로 내보낸다.
2. action 함수는 export로 내보낸다.
3. 액션 타입을 정할 때, reducer/ACTION_TYPE 형태로 적는다.

이러한 규칙을 지켜 하나의 파일에 한 가지 기능에 대한 내용을 작성한다.

```typescript
// ducks 패턴

const INCREASE = "counter/INCREASE" as const;
const DECREASE = "counter/DECREASE" as const;
const INCREASE_BY = "counter/INCREASE_BY" as const;

export const increase = () => ({
  type: INCREASE,
});

export const decrease = () => ({
  type: DECREASE,
});

export const increaseBy = (diff: number) => ({
  type: INCREASE_BY,
  payload: diff,
});

type CounterAction =
  | ReturnType<typeof increase>
  | ReturnType<typeof decrease>
  | ReturnType<typeof increaseBy>;

type CounterState = {
  value: number;
};

const initialState: CounterState = {
  value: 0,
};

function counter(
  state: CounterState = initialState,
  action: CounterAction,
): CounterState {
  switch (action.type) {
    case INCREASE:
      return { value: state.value + 1 };
    case DECREASE:
      return { value: state.value - 1 };
    case INCREASE_BY:
      return { value: state.value + action.payload };
    default:
      return state;
  }
}

export default counter;

```



## Redux-saga

![image](https://uzilog-upload.s3.ap-northeast-2.amazonaws.com/private/ap-northeast-2%3Ab6c10628-1f45-492c-a9eb-f54020bc8014/1583937319450-image.png)

React는 앱이 가벼울 경우에 react-hook을 사용하여 state 핸들링을 손 쉽게 할 수 있다. 그러나 복잡한 구조의 컴포넌트를 구현하는 데 있어 prop을 사용한 데이터 단방향 전달은 경우에 따라 수번 내지 10번 이상의 전달이 이루어질 수도 있다. 이는 `prop drilling`이라 하며, 컴포넌트간의 구멍을 송송 뚫어서 그렇다랄까, 느낌이 잘 와닿는 단어 표현이다. 

이렇게 `prop drilling`이 심한 경우, 혹은 단일 컴포넌트만 사용하는 state가 아닌 경우, 이 상태를 전역적으로 관리할 필요가 생긴다. 이를 돕기 위한 라이브러리로는 `Context Api`, `Recoil`, `Mobx` 등이 있는데, 이 중에서 이번에 사용할 것은 `Redux`이다.

그러나 store에 데이터를 관리하던 중, 앱이 복잡해지며 비동기 처리를 해야 하는 코드가 생기게 되는 경우에, React와 Redux 그 중간에 이런 비동기 처리 로직을 어디에서 관리해야 할 지에 대한 의문이 생긴다. 😥

이런 문제를 해결하는 라이브러리로 `React-thunk`, `Redux-Saga`가 있는데, 둘 다 Middleware의 역할을 수행한다. 아래는 갱장갱장 유명한 `gif`이다.

![](https://miro.medium.com/max/1400/1*QERgzuzphdQz4e0fNs1CFQ.gif)

Middleware에서 Action과 Reducer사이의 과정을 수행한다는 것이다. 예를 들어 무차별 클릭 연타를 통해 서버를 위험하게 하는 동작들을 Reducer가 실행되기 이전에 이를 방지한다는 것이다.(`개쩐다`)

- Redux-Saga

> Redux-saga는 애플리케이션에서 일어나는 Side Effects를 쉽게 관리하며 효과적인 실행, 손쉬운 테스트 그리고 에러 핸들링을 쉽게 해준다.

	#### Middleware

Redux-Saga는 View를 담당하는 `React`와 데이터를 관리하는 `Redux` 사이에서 뭔가를 조작한다.

`사이` 에서라는 말은 정말 중요한데, 이는 `Redux-Saga`가 middleware로서 조작을 한다는 것을 의미하기 때문이다.

#### Generator

Saga는 제너레이터를 이용하여 이 역할을 수행한다.

#### Effects

이는 이벤트를 처리할 내용을 담는다. Redux-Saga 에서는 이러한 이펙트를 `yield`를 통해 호출하고 수행된 내용을 다시 돌려받아 그 다음 액션을 수행한다. 즉, Saga는 제너레이터를 통해 이펙트를 수행한다고 볼 수 있다. 이런 이펙트로는 `take`, `call`, `put` 등이 있다.

#### ComposeEnhancers와 ComposeWithDevtools의 차이

는 다음 시간에!