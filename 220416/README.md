# React native

Core Components

- Basic Components

  1. `View`

     - UI 구축을 위한 가장 기본적인 `container`. UIView, <div>, android.view 등 어떤 플랫폼에서든 기본 보기에 매핑시킨다.

     - inline style도 지원하나, 명확성과 성능을 위해 StyleSheet과 함께 사용하도록 설계되었음.

       ---

       ##### Critical Props

       - onLayout
       
         -  마운트 및 레이아웃 변경시 호출.
       
         >Type: ({nativeEvent: LayoutEvent}) => void

---

#### Style override

```react
<View style={[styles.centeredView, { justifyContent: "center" }]}>
```

이런 식으로 사용 가능