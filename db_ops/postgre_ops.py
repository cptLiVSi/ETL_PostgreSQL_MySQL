from db_ops.db_ops_abstract import DbOpsAbstract


class PostgreOps(DbOpsAbstract):
    def __init__(self, adapter, login, password, port, host_, db_name):
        self.rdbms_type = 'postgresql'
        super().__init__(self.rdbms_type, adapter, login, password, port, host_, db_name)
