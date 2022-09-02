# To run the project

поднимаем контейнера
через бобер коннект к Postgre и MySQL

PostgreSQL:
```
login = 'postgres'
pas = 'example'
port = '5432'
```

MySQL:
```
login = 'root'
pas = 'mysql'
port = '3306'
```

создаем БД в Postgre: northwind, p1, p2;
в mysql: m1, m2.

# Working process
запускаем app.py
что происходит:

создаются таблицы в базе northwind

таблицы копируется 4 раза:
1. внутри posgre      (nw -> p1)
2. postgre - mysql    (p1 -> m1)
3. внутри mysql       (m1 -> m2)
4. mysql - postgre    (m2 -> p2)
