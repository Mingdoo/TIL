# TIL

> multiple reference (`React`)

내 코드

```typescript

const zoomableViewRef: any = useRef([]);

const index = ({ imageUrls, style }: any) => {
  const zoomableViewRef: any = useRef([]);

  return (
    <>
      {imageUrls.map((url, idx) => (
        <View style={style} key={idx}>
          <ReactNativeZoomableView
            bindToBorders={true}
            doubleTapZoomToCenter={true}
            maxZoom={1.5}
            ref={(element) => (zoomableViewRef.current[idx] = element)}
            onZoomEnd={() => zoomableViewRef.current[idx]!.zoomTo(1)}
            pinchToZoomInSensitivity={9}
            pinchToZoomOutSensitivity={9}
            zoomCenteringLevelDistance={1.5}
          >
            ...
          </ReactNativeZoomableView>
        </View>
      ))}
    </>
  );
};
```

multiple reference를 사용해야할때!

```typescript
ref={(element) => (zoomableViewRef.current[idx] = element)}
```

부분을 사용해서 reference부분을 해결했습니다.



> Pinch zoom (`Expo`)

ReactNativeZoomableView + pager view를 사용해서 carousel을 만들었음.