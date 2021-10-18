# SQLite3
- table 생성

```sqlite
-- table 생성
CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- null은 들어갈수 없음! 그걸 설정하자 / AUTOINCREMENT는 자동으로 id가 올라감
CREATE TABLE classmates (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
```

- table 삭제

```sqlite
DROP TABLE classmates;
```

- table 정보 설정

```sqlite
-- csv파일 정보를 적용
.mode csv
.import users.csv users
.tables
```

- 전체 데이터 조회

```sqlite
-- 전체 데이터 조회
SELECT * FROM classmates;
-- rowid와 함께 모두 보는방법
SELECT rowid, * FROM classmates;
```

- 데이터 생성(`C`)

```sqlite
-- CREATE
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
-- 넣는 데이터의 개수가 컬럼의 개수와 동일하다면 컬럼 이름을 생략할 수 있음.
INSERT INTO classmates VALUES ('강민수', 26, 'SEOUL');

```

- 데이터 읽기(`R`)

```sqlite
-- READ

-- 2개만
SELECT rowid, name FROM classmates LIMIT 2;
-- 앞의 1개 제외하고 2개만
SELECT rowid, name FROM classmates LIMIT 200 OFFSET 1;
-- Where
SELECT rowid, name FROM classmates WHERE address='서울' OR address='SEOUL';
SELECT rowid, name FROM classmates WHERE age >= 30;

-- 중복없이 고유한 값만 (DISTINCT)
SELECT DISTINCT age FROM classmates;
```

- 데이터 수정(`U`)

```sqlite
-- UPDATE
UPDATE classmates SET name='강민수' WHERE address='서울'
```

- 데이터 삭제(`D`)

```sqlite
-- DELETE
DELETE FROM classmates WHERE rowid=1;
```

- Where 절

```sqlite
-- WHERE 절
CREATE TABLE users (
   ...> first_name TEXT NOT NULL,
   ...> last_name TEXT NOT NULL,
   ...> age INTEGER NOT NULL,
   ...> country TEXT NOT NULL,
   ...> phone TEXT NOT NULL,
   ...> balance INTEGER NOT NULL);
```

- 그밖에 여러가지 `READ`

```sqlite
-- COUNT
SELECT COUNT(*) FROM users;

-- AVG 
SELECT AVG(balance) FROM users where age >= 30;

-- MAX 내놔 이름, 제일(balance) 큰애 어디서 유저에서
SELECT first_name, MAX(balance) FROM users;

-- LIKE (내놔 *(다) 어디서 유저에서 WHERE(근데) 핸드폰 LIKE(어떻게) 요롷게 생긴애)
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE phone LIKE '%-5114-%';
SELECT * FROM users WHERE age LIKE '2_';

-- ORDER BY (순서에 따라 다르다!)
SELECT * FROM users ORDER BY last_name, age ASC LIMIT 10;
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

-- GROUP BY (요약행을 만든다!)
SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```

