## To run the project

поднимаем контейнера
через бобер коннект к Postgre и MySQL

Postgre:
```
login = 'postgres'
pas = 'example'
port = '5432'
```

My:
```
login = 'root'
pas = 'mysql'
port = '3306'
```

ручками врукопашную в бобре создем в Postgre БД `northwind`:
запускаем SQL скрипт - копипаста из nortwhind2.txt

создаем БД в Postgre: p1, p2;
в mysql: m1, m2.

# Working process
запускаем main.py
чо происходит:

таблица копируется 4 раза:
1. внутри posgre      (nw -> p1)
2. postgre - mysql    (p1 -> m1)
3. внутри mysql       (m1 -> m2)
4. mysql - postgre    (m2 -> p2)
5. ???
6. PROFIT!!!