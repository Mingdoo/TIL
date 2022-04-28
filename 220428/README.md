# TIL

expo Date Time Picker

### install

```bash
expo install @react-native-community/datetimepicker
```

> 총평 : 대환장 신기함

Android와 iOS는 서로 다른 운영체제라, 각자의 UI 세계관을 갖고 있다. 둥글둥글한 아이폰과 조금은 딱딱해보이는 안드로이드. react-native는 결국 이 운영 체제 위에 올라가는 앱이기 때문에 브릿지를 통해 자바스크립트를 운영체제와 소통하도록 만들어야 한다.

이 때, date picker의 사용을 보게 되면, 안드로이드 내장 date time picker와 아이폰의 이것이 서로 다른데, 이 브릿지를 통해 react native date time picker는 직접 구현된 것이 아닌 운영체제에 맞는 date time picker를 불러주고, 이 정보를 받아오는 방법으로 사용한다.

안드로이드는 모달창이 직접 떠서 사용되고, iOS는 모달이 뜨기 전 시간을 보여주는 기능을 내장하고 있는데, 여기서 문제가 생긴다. **모달 띄우기 시러잉!**

결국 Device가 어떤 운영체제인지 확인하고, 이를 분리해 구현해야 할 것이다.

### 해결

```react
{Device.osName === "Android" && (
    <DateTimeAndroid
        functions={{ setTimeOpen, setDateOpen }}
        states={{ timeOpen, dateOpen }}
        date={date}
        />
)}
```

이런 식으로 해결했다. state로 모달 창이 열렸는지 아닌지를 확인하고, 이를 iOS와 Android 둘 다 적용하기 위해 iOS는 항상 모달이 열려있는 방법으로 구현했는데, 뭐.. 만족!