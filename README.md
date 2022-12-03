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

<a name="s5"></a>
таблица копируется 4 раза:
1. внутри posgre      (nw -> p1)
2. postgre - mysql    (p1 -> m1)
3. внутри mysql       (m1 -> m2)
4. mysql - postgre    (m2 -> p2)
5. ???
6. PROFIT!!!



## Implemented adapters
| Service                  | Config example                                        |
|--------------------------|-------------------------------------------------------|
| Athena                   | [config](config_examples/athena.yaml)                 | <a name="athena"></a>
| DynamoDB                 | [config](config_examples/dynamodb.yaml)               | <a name="dynamodb"></a>
| Glue                     | [config](config_examples/glue.yaml)                   | <a name="glue"></a>
| Kinesis                  | [config](config_examples/kinesis.yaml)                | <a name="kinesis"></a>
| Quicksight               | [config](config_examples/quicksight.yaml)             | <a name="quicksight"></a>
| S3                       | [config](config_examples/s3.yaml)                     | <a name="s3"></a>
| Sagemaker                | [config](config_examples/sagemaker.yaml)              | <a name="sagemaker"></a>
| SQS   <a name="sqs"></a> | [config](config_examples/sqs.yaml)                    |
| SagemakerFeaturestore    | [config](config_examples/sagemaker_featurestore.yaml) | <a name="sagemaker_featurestore"></a>