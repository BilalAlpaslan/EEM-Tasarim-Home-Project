import sqlite3


class HomeDB():
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def create_table(self, table_name, fields):
        sql = 'CREATE TABLE IF NOT EXISTS %s (%s)' % (table_name, fields)
        self.execute(sql)
