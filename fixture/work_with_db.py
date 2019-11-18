import psycopg2
from psycopg2.extras import DictCursor
from contextlib import closing
from model.input_data import *
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import time


class DbHelper:

    def __init__(self, host=None, dbname=None, user=None, password=None, records=None, image=None):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.records = records
        self.connection = closing(psycopg2.connect(host=host, dbname=dbname, user=user, password=password))
        self.connection.autocommit = True
        self.image = 'image'

    def create_db(self):
        con = psycopg2.connect(dbname='postgres', user=self.user, host=self.host, password=self.password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
        cur = con.cursor()
        # Удалить БД если уже есть
        cur.execute('DROP DATABASE IF EXISTS image')
        # Use the psycopg2.sql module instead of string concatenation
        # in order to avoid sql injection attacs.
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.image)))

    def create_tables(self):
        with self.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('CREATE TABLE IF NOT EXISTS public.image(tid integer, image bytea)')
                conn.commit()
                # cursor.close()

    def drop_db(self):
        con = psycopg2.connect(dbname='postgres', user=self.user, host=self.host, password=self.password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(self.image)))

    def check_db(self):
        db = DbHelper(host="localhost", user="postgres", dbname="image", password="postgres")

        with db.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM image WHERE tid=%s', (tid,))
                db.records = cursor.fetchall()
                # print(self.records)
        return 0

    def clean_db(self):
        with self.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM image WHERE tid=%s', (tid,))
                conn.commit()

    def create_db_and_tables(self):
        db = DbHelper(host="localhost", user="postgres", password="postgres")
        db.create_db()
        db = DbHelper(host="localhost", user="postgres", dbname="image", password="postgres")
        time.sleep(5)
        db.create_tables()
