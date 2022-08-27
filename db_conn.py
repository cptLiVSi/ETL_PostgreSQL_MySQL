import pandas as pd
from sqlalchemy import create_engine


class DbConn:
    def __init__(self, connector, login, password, port, host_, db_name):
        self.connector = connector
        self.login = login
        self.password = password
        self.port = port
        self.host = host_
        self.db_name = db_name
        self.connection = create_engine(
            fr'{self.connector}://{self.login}:{self.password}@{self.host}:{self.port}/{self.db_name}')

    def copy_self_db_to(self, output_conn):
        if self.connector == 'postgresql+psycopg2':
            query = "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != " \
                    "'information_schema'; "
            table_name = 'tablename'
        if self.connector == 'mysql+pymysql':
            query = "SHOW TABLES"
            table_name = f'Tables_in_{self.db_name}'
        list_of_tables = pd.read_sql(query, self.connection)
        for i in list_of_tables[table_name]:
            df_to_copy = pd.read_sql(f'SELECT * FROM {i}', self.connection)
            df_to_copy.to_sql(f'{i}', output_conn.connection, if_exists="replace", index=False)
