from postgre_ops import PostgreOps
from mysql_ops import MysqlOps

post_adapter = 'psycopg2'
post_login = 'postgres'
post_pas = 'example'
post_port = '5432'
post_host = 'localhost'

mysql_adapter = 'pymysql'
mysql_login = 'root'
mysql_pas = 'mysql'
mysql_port = '3306'
mysql_host = 'localhost'


nw = PostgreOps(post_adapter, post_login, post_pas, post_port, post_host, 'northwind')
p1 = PostgreOps(post_adapter, post_login, post_pas, post_port, post_host, 'p1')
p2 = PostgreOps(post_adapter, post_login, post_pas, post_port, post_host, 'p2')
m1 = MysqlOps(mysql_adapter, mysql_login, mysql_pas, mysql_port, mysql_host, 'm1')
m2 = MysqlOps(mysql_adapter, mysql_login, mysql_pas, mysql_port, mysql_host, 'm2')


nw.open_connection()
nw.query(open(r"docker_env/northwind2.txt", "r").read())
nw.commit()
nw.close_connection()

nw.copy_all_to(p1)
p1.copy_all_to(m1)
m1.copy_all_to(m2)
m2.copy_all_to(p2)
