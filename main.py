from db_conn import DbConn

post_conn = 'postgresql+psycopg2'
post_login = 'postgres'
post_pas = 'example'
post_port = '5432'

mysql_conn = 'mysql+pymysql'
mysql_login = 'root'
mysql_pas = 'mysql'
mysql_port = '3306'

host = 'localhost'

nw_dbc = DbConn(post_conn, post_login, post_pas, post_port, host, "northwind")

p1_dbc = DbConn(post_conn, post_login, post_pas, post_port, host, "p1")
p2_dbc = DbConn(post_conn, post_login, post_pas, post_port, host, "p2")
p3_dbc = DbConn(post_conn, post_login, post_pas, post_port, host, "p3")

m1_dbc = DbConn(mysql_conn, mysql_login, mysql_pas, mysql_port, host, "m1")
m2_dbc = DbConn(mysql_conn, mysql_login, mysql_pas, mysql_port, host, "m2")
m3_dbc = DbConn(mysql_conn, mysql_login, mysql_pas, mysql_port, host, "m3")

nw_dbc.copy_self_db_to(p1_dbc)
p1_dbc.copy_self_db_to(m1_dbc)
m1_dbc.copy_self_db_to(m2_dbc)
m2_dbc.copy_self_db_to(p2_dbc)
