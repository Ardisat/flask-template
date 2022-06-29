import pymysql
from pymysql.cursors import DictCursor



dbh = pymysql.connect(
    host='host',
    user='username',
    password='password',
    db='database',
    charset='utf8mb4',
    cursorclass=DictCursor,
    autocommit=True
)



def execute(sql):
    try:
        with dbh.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            out_data = {
                'status': 'ok', 
                'data': rows
            }
    except Exception as e:
        out_data = {
            'status': 'error',
            'data': str(e)
        }

    return out_data