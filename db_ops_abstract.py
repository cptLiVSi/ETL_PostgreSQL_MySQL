import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect


class DbOpsAbstract:
    def __init__(self, rdbms_type, adapter, login, password, port, host_, db_name):
        self.rdbms_type = rdbms_type
        self.adapter = adapter
        self.login = login
        self.password = password
        self.port = port
        self.host = host_
        self.db_name = db_name
        self.connection = None
        self.engine = create_engine(
            fr'{self.rdbms_type}+{self.adapter}://{self.login}:'
            fr'{self.password}@{self.host}:{self.port}/{self.db_name}')

    def open_connection(self):
        self.connection = self.engine.connect()

    def query(self, query):
        return self.connection.execute(query)

    def close_connection(self):
        self.connection.close()

    def get_table_names(self):
        return inspect(self.engine).get_table_names()

    def copy_table_to(self, db, table_name):
        df_to_copy = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)
        df_to_copy.to_sql(f'{table_name}', db.engine, if_exists="replace", index=False)

    def commit(self):
        self.connection.begin().commit()

    def create_db(self, db_name):
        pass

    def copy_all_to(self, db):
        tables = self.get_table_names()
        for i in tables:
            self.copy_table_to(db, i)
