# Riot api handling



development key : 

> 비밀~



라이엇 api를 이용해서 나의 정보를 가져오자. 최근 전적, 스펠, 특성 등 여러 정보를 얻어보자. 그러기 위해선 먼저 해야 할 것이 있다. 바로 `development key` 를 받아오는것.

- [라이엇 개발자 포털](https://developer.riotgames.com/)

위의 사이트로 이동해서 본인이 사용하는 롤 계정으로 로그인을 해서 key를 받아오자.

개인 `development key`는 다른 사람에게 절대 공유하지 말자.

그 다음, 터미널을 통해

```bash
$ pip install riotwatcher
```

로 사용하는 파이썬에 riotwatcher 모듈을 다운로드 받도록 하자.



아래의 코드를 통해 정보를 얻어올 준비를 하면 된다.

```python
api_key = '<private development key>'
watcher = Lolwatcher(api_key)
my_region = 'KR'

my_account = watcher.summoner.by_name(my_region, '<사용하는 닉네임>')
```

만약 다른 서버를 사용중이라면, [서버 목록](https://developer.riotgames.com/docs/lol)을 참고해서 my_region부분을 바꾸도록 하자.



my_account의 데이터 형태를 간단하게 보자.

```json
{
    'id': '_9816JY7i3MmWMVax17K22bNJQ9RJ2vrNtAY0Y2Di6iL4g',
 	'accountId': 'PU0uDzGwQSQuH0CnxAC2H81JjAKz3bACb-X6O_-8DAjF',
 	'puuid': 'osGVqQWwg30m-sBfZdOPYFyGhMzrCOy1Ft32ZrZ9h4HerLLlq0JIPsqX_4kuBFGELBvKmw8qA_v2PA',
 	'name': '갓 민 수 임',
 	'profileIconId': 7,
 	'revisionDate': 1626683526000,
 	'summonerLevel': 121,
}
```

크게

- Id : encrypted id
- accountId : unique for my region
- puuid : unique for global

정도로 구분할 수 있다.



나의 랭크 정보를 알아오는 코드는 다음과 같다.

```python
my_rank_stats = watcher.league.by_summoner(my_region, my_id)
```

이를 pprint로 출력해보면 다음과 같은 결과가 나온다.

```json
{
    'freshBlood': False,
 	'hotStreak': False,
 	'inactive': False,
	 'leagueId': 'e9a2a5e5-1596-4165-8b03-95942b7fb6c7',
	 'leaguePoints': 63,
	 'losses': 9,
	 'queueType': 'RANKED_SOLO_5x5',
	 'rank': 'IV',
	 'summonerId': '_9816JY7i3MmWMVax17K22bNJQ9RJ2vrNtAY0Y2Di6iL4g',
	 'summonerName': '갓 민 수 임',
	 'tier': 'SILVER',
	 'veteran': False,
	 'wins': 8,
}
```

여기서 queue가 알고있는 큐가 아니라 그냥 큐 잡는 그 큐같다.



다음은 내가 했던 경기 목록을 보자.

```python
my_matches = watcher.match.matchlist_by_account(my_region, my_accountId)

pprint.pprint(my_matches['matches'][0])
```

결과는

```json
{
    'champion': 102,
	 'gameId': 5335608190,
	 'lane': 'JUNGLE',
	 'platformId': 'KR',
	 'queue': 430,
	 'role': 'NONE',
	 'season': 13,
	 'timestamp': 1626707269673,
}
```

가 나왔다. 'champion' 부분이 숫자라서 뭔가 했는데 102번은 쉬바나였다. 마지막 판에 쉬바나를 했나보다.



```python
participants = []
n = 0
for row in match_detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Id']
    participants_row['spell2'] = row['spell2Id']
    participants_row['win'] = row['stats']['win']
    participants_row['kills'] = row['stats']['kills']
    participants_row['deaths'] = row['stats']['deaths']
    participants_row['assists'] = row['stats']['assists']
    participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    participants_row['goldEarned'] = row['stats']['goldEarned']
    participants_row['champLevel'] = row['stats']['champLevel']
    participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    participants_row['item0'] = row['stats']['item0']
    participants_row['item1'] = row['stats']['item1']
    participants_row['summonerName'] = match_detail['participantIdentities'][n]['player']['summonerName']
    n+=1
    participants.append(participants_row)
    
df = pd.DataFrame(participants)

import numpy as np
df.index = np.arange(1,len(df)+1)
```

마지막 판 정보를 다 가져와봤다. 이를 pandas 모듈로 dataframe화 시킬 수 있는데, 

```
champion  spell1  spell2    win  kills  deaths  assists  totalDamageDealt  \
76      14       4   True      5       1        6             98538   
517      12       4   True      2       4        4             97513   
234      11       4   True      8       1        3            126737   
63      14       4   True      5       3       10             69413   
22       7       4   True      8       1        3            106703   
517      12       4  False      1       6        2             44185   
102       4      11  False      2       5        2            114131   
350      14       3  False      0       5        4             13335   
83      14       4  False      5       4        0            108777   
67       7       4  False      2       8        2             56254   

    goldEarned  champLevel  totalMinionsKilled  item0  item1 summonerName  
        10171          14                 148   2031   6632          랩 동  
         8193          13                 136   6656   2033  		Goldteacher  
         9747          13                  10   6632   2031    		SouthTown  
         9259          12                  43   2031   3157        복숭코코팜  
        10607          12                 156   1055   3046     	죽지못해사는인간  
         5231          10                  66   6656   1052         빨간브라  
         7564          12                  77   3115   2031      	갓 민 수 임  
         4608          10                   2   3853   6617      	 TRIICK  
        10294          14                 175   3111   6692      	 군용 슬리퍼  
         6289          10                 107   1055   6673      	 와퍼왕버거킹  
```

이런식으로 데이터가 나오는 것을 알 수 있다.

실제로, match_detail을 print해보면 훨씬 많은 정보들이 들어있음을 알 수 있다. ex) `towerKills`, `dragonKills`등 정말 세세한 정보를 얻어올 수 있다.



이제는, 챔피언 번호와 이름을 매칭해보자.

- latest : 지역에 맞는 버전을 받아온다.
- champ_list : 챔피언 리스트를 받아온다.

```python
latest = watcher.data_dragon.versions_for_region('na1')
champ_list = watcher.data_dragon.champions(latest['n']['champion'])
```

champ_list는 생각보다 진짜 너무 더럽다. 여러 정보들을 갖고있는데, 초기설정부터 이름, 번호까지 대부분의 정보를 갖고있다고 보면 된다.

이제는 champ_list['data']에 있는 번호와 이름을 새로운 champ_dict에 담아보도록 하자.

```python
champ_list
champ_dict = {}
for key in champ_list['data']:
    row = champ_list['data'][key]
    champ_dict[row['key']] = row['id']

for row in participants:
    row['championName'] = champ_dict[str(row['champion'])]
    
df = pd.DataFrame(participants)
print(df)
```

결과는 다음과 같다.

```
champion  spell1  spell2    win  kills  deaths  assists  totalDamageDealt  \
	76      14       4   True      5       1        6             98538   
	517      12       4   True      2       4        4             97513   
	234      11       4   True      8       1        3            126737   
	63      14       4   True      5       3       10             69413   
	22       7       4   True      8       1        3            106703   
	517      12       4  False      1       6        2             44185   
	102       4      11  False      2       5        2            114131   
	350      14       3  False      0       5        4             13335   
	83      14       4  False      5       4        0            108777   
	67       7       4  False      2       8        2             56254   

    goldEarned  champLevel  totalMinionsKilled  item0  item1 summonerName  \
        10171          14                 148   2031   6632          랩 동   
         8193          13                 136   6656   2033  Goldteacher   
         9747          13                  10   6632   2031    SouthTown   
         9259          12                  43   2031   3157        복숭코코팜   
        10607          12                 156   1055   3046     죽지못해사는인간   
         5231          10                  66   6656   1052         빨간브라   
         7564          12                  77   3115   2031      갓 민 수 임   
         4608          10                   2   3853   6617       TRIICK   
        10294          14                 175   3111   6692       군용 슬리퍼   
        6289          10                 107   1055   6673       와퍼왕버거킹   

   championName  
       Nidalee  
         Sylas  
         Viego  
         Brand  
          Ashe  
         Sylas  
       Shyvana  
         Yuumi  
        Yorick  
        Vayne  
```

생각해보니 내가 쉬바나로 엄청난 똥을 쌌던 기억이 났다.

api 공부는 여기서 끝내야겠다.

