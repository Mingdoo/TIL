# cs(DB)

## Join

조인

> 두 개 이상의 테이블이나 db를 연결하여 데이터를 검색하는 방법

연결하려면, 적어도 하나의 컬럼을 공유해야 함.

### Join 종류

- inner join
- left outer join
- right outer join
- full outer join
- cross join
- self join



- ### Inner Join

교집합

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile9.uf.tistory.com%2Fimage%2F99799F3E5A8148D7036659)

```sql
SELECT
A.NAME, B.AGE
FROM A INNER JOIN B ON A.NO_EMP = B.NO_EMP
```

- ### Left Outer Join

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile6.uf.tistory.com%2Fimage%2F997E7F415A81490507F027)

```sql
SELECT A.NAME, B.AGE
FROM A LEFT OUTER JOIN B ON A.NO_EMP = B.NO_EMP
```

- ### Right Outer Join

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile25.uf.tistory.com%2Fimage%2F9984CE355A8149180ABD1D)

```sql
SELECT
A.NAME, B.AGE
FROM EX_TABLE A
RIGHT OUTER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP
```

- ### Full Outer Join

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F99195F345A8149391BE0C3)

합집합

- ### Cross Join

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F993F4E445A8A2D281AC66B)

```sql
SELECT A.NAME, B.AGE
FROM A CROSS JOIN B
```

결과 : 하나씩 컬럼 BY 컬럼 (총 12개)



## SQL Injection

> 해커에 의해 조작된 SQL 쿼리문이 데이터베이스에 그대로 전달되어 비정상적 명령을 실행시키는 공격 기법

#### 공격 방법

1. 인증 우회

SQL Injection으로 공격할 때, input 창에 비밀번호를 입력함과 동시에 다른 쿼리문을 함께 입력하는 것이다.

```sql
SELECT * FROM USER WHERE ID = 'ABD' AND PASSWORD = '1234'; DELETE * USER FROM ID = '1';
```



2. 데이터 노출

시스템에서 발생하는 에러 메세지를 이용해 공격하는 방법.

GET방식으로 동작하는 URL쿼리 스트링을 추가하여 에러를 발생.



#### 방어 방법

1. INPUT값을 받을 때, 특수문자 여부 검사

> 로그인 전, 검증 로직을 추가하여 미리 설정학 특수문자들이 들어왔을 때 요청을 막아낸다.

2. SQL서버 오류 발생 시, 에러 메세지 감추기
3. PREPARESTATEMENT 사용하기



## SQL과 NOSQL의 차이

spring에서는 MySQL을, Node.js에서는 MongoDB를 주로 사용한다.

### SQL(RDBMS)

SQL을 사용하면 RDBMS에서 데이터를 저장, 수정, 삭제 및 검색할 수 있음.

- 데이터는 정해진 데이터 스키마에 따라 테이블에 저장된다.
- 데이터는 관계를 통해 여러 테이블에 분산된다.

데이터는 테이블에 레코드로 저장되는데, 각 테이블마다 명확하게 정의된 구조가 있음.

그래서 스키마를 준수하지 않은 레코드는 테이블에 추가할 수 없다.

데이터의 중복을 피하기 위해 `관계`를 사용한다.

![img](https://t1.daumcdn.net/cfile/tistory/994D09355C937ECD2D)

하나의 테이블에서 중복 없이 하나의 데이터만을 관리하기 때문에 다른 테이블에서 부정확한 데이터를 다룰 위험이 없어지는 장점이 있다.



### NoSQL(비관계형 DB)

스키마도 없고, 관계도 없다.

NoSQL에서 레코드를 문서(documents)라고 부른다.

SQL은 정해진 스키마를 따르지 않으면 데이터 추가가 불가능했지만, NoSQL에서는 다른 구조의 데이터를 같은 컬렉션에 추가할 수 있다.

문서는 Json과 비슷한 형태로 가지고 있다. 관계형 데이터베이스처럼 여러 테이블에 나누어 담지 않고, 관련 데이터를 동일한 컬렉션에 담는다.

따라서 위 사진에 SQL에서 진행한 Orders, Users, Products 테이블로 나눈 것을 NoSQL에서는 Orders에 한꺼번에 포함해서 저장하게 된다.

조인하고 싶을 때 NoSQL은 어떻게 할까??

> 컬렉션을 통해 데이터를 복제하여 각 컬렉션 일부분에 속하는 데이터를 정확하게 산출하도록 한다.

데이터가 중복되어 서로에게 위험을 줄 위험이 있다. 따라서 조인을 잘 사용하지 않고 자주 변경되지 않는 데이터일 때  NoSQL을 쓰면 효율적이다.



### 확장 개념

두 DB를 비교할 때 중요한 Scaling개념도 존재한다.

DB server의 확장성은 `수직적`확장과 `수평적`확장으로 나누어진다.

- 수직적 : 단순히 db 서버의 성능을 향상시키는 것(cpu 업글 등)
- 수평적 : 더 많은 서버가 추가되고 db가 전체적으로 분산됨을 의미(하나의 데이터베이스에서 작동하지만 여러 호스트)



데이터 저장 방식으로 인해 SQL 데이터베이스는 수직적 확장만 지원함

> 수평적 확장은 NoSQL에서만 가능



#### SQL 장점

- 명확하게 정의된 스키마, 데이터 무결성 보장
- 관계는 각 데이터를 중복 없이 한번마 저장



#### SQL 단점

- 덜 유연함. 데이터 스키마를 사전에 계획하고 알려야 함(나중에 수정하기 힘듬).
- 관계를 맺고있어서 조인문이 많은 복잡한 쿼리가 만들어질 수 있음.

> 쿼리 : 쉽게 이야기해서 데이터베이스에 정보를 요청하는 것입니다. 쿼리(Query)는 웹 서버에 특정한 정보를 보여달라는 웹 클라이언트 요청(주로 문자열을 기반으로 한 요청)에 의한 처리입니다. 쿼리(Query)는 대개 데이터베이스로부터 특정한 주제어나 어귀를 찾기 위해 사용됩니다. 주제어가 검색엔진의 검색필드 내에 입력된 다음, 그 내용이 웹 서버로 넘겨집니다.
>
> **[출처]** [쿼리(Query)란 무엇인가?](https://blog.naver.com/rlarbtjq7913/221805728231)|**작성자** [김자까](https://blog.naver.com/rlarbtjq7913)



#### NoSQL 장점

- 스키마가 없어서 유연함. 언제든지 저장된 데이터를 조정하고 새로운 필드 추가 가능.
- 데이터는 애플리케이션이 필요로 하는 형식으로 저장됨. 데이터 읽어오는 속도 빨라짐
- 수직 수평 확장이 모두 가능해서 애플리케이션이 발생시키는 모든 읽기 쓰기 요청 처리가 가능.



#### NoSQL 단점

- 유연성으로 인해 데이터 구조 결정을 미루게 될 수 있음
- 데이터 중복을 계속 업데이트 해야함
- 데이터가 여러 컬렉션에 중복되어 있기 떄문에 수정 시 모든 컬렉션에서 수행해야 함