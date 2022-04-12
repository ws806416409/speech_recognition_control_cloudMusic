"""
@Time       ：2022/4/12 16:13 
@File       ：db.py
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""
import pymysql


class Db:
    def __init__(self):
        self.host = "47.97.231.180"
        self.user = "root"
        self.password = "root"
        self.database = "wyy"
        self.port = 3310
        self.mdb = pymysql.connect(
            host = self.host,
            user = self.user,
            port=self.port,
            password = self.password,
            database = self.database,
        )
        print("connect")
        return

    def insert_info(self, id, age, gender, city, comment):
        cursor = self.mdb.cursor()
        if id and age and gender and city and comment:
            string = "'%s','%s','%s','%s','%s'" % (id, age, gender, city, comment)
            sql ='INSERT INTO music_comment (id, age, gender, city, comment) VALUES (%s)' % string
            print('sql:', sql)
            cursor.execute(sql)
            self.mdb.commit()
            return 1
        else:
            return -1