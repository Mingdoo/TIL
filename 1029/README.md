# Django-serialization

`Serialization` : 효율적인 valid검사, queryset에서 불러오는 것을 구현할 수 있음. `Django`의 form과 비슷함!



#### Serializer

> Serialize(직렬화)
>
> Queryset, Model instance 등의 복잡한 데이터를 Json, XML등의 content type으로 변환 가능한 python datatype으로 변환시켜줌
>
> > Django에서 사용하는 파이썬 객체나 queryset을 REST api에서 사용하는 json형태로 변환해주는 역할을 한다.
>
> Deserialize
>
> 받은 데이터(크롤링시 parser를 사용해서 python datatype)를 validating한 후에 parsed data를 complex type으로 다시 변환한다.
>
> 이 때는, serializer의 is_valid()를 사용하여 검사하자.
>
> 추가로, is_valid() 안에 raise_exception=True를 통해 exception이 발생 할 때, return하는 response를 바로 구현할 수 있음.

#### Implementation

```python
#in serializers.py
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

#in views.py
@api_view(['GET','POST'])
def actor_list_or_create(request):
    def actor_list():
        actors = Actor.objects.all()
        #many=True를 사용하는 이유는 queryset이 여러개일 수 있기 때문.
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    def create_actor():
        serializer = ActorSerializer(data=request.data)
        #raise_exception을 통해 response를 보낼 수 있음.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'GET':
        return actor_list()
    elif request.method == 'POST':
        return create_actor()
```

> 1. [`{address/api/v1/`]로 들어온 request는 `urls.py`를 타고 movies의 `urls.py`로 들어간다.
> 2. `movies/urls.py`는 `url_patterns`에 맞게 path를 통해 `views.py`의 적절한 메소드를 호출한다.
> 3. 호출에 응답하는 함수(위에서는 `actor_list_or_create`)는 `serialzers.py`의 `ActorListSerializer`를 호출하며 Actor 모델에 있는 데이터(`queryset`)를 직렬화하여 데이터를 response에 담아 보낸다.
> 4. response 내에는 Json형태의 데이터가 되어 응답을 받을 수 있다.
