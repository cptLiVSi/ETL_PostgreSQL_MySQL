# To run the project

```docker-compose -f ./docker_env/docker-compose.yml up -d```

via DBeaver manually connect to PosgtreSQL, MySQL:

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


# Working process
launch app.py:

* databases nw, p1, p2, m1, m2 are being created;
* tables in northwind are being created;
* tables are copied 4 times:

1. within posgtre     (nw -> p1)
2. postgre - mysql    (p1 -> m1)
3. within mysql       (m1 -> m2)
4. mysql - postgre    (m2 -> p2)
