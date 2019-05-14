import psycopg2
from psycopg2.extras import DictCursor
from contextlib import closing
from model.input_data import *


class DbHelper:

    def __init__(self, host=None, dbname=None, user=None, password=None, records=None):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.records = records
        self.connection = closing(psycopg2.connect(host=host, dbname=dbname, user=user, password=password))
        self.connection.autocommit = True

    def check_db(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM image WHERE tid=%s', (tid,))
                self.records = cursor.fetchall()
                # print(self.records)
        return 0



    def clean_db(self):
        with self.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM image WHERE tid=%s', (tid,))
                conn.commit()



