import time
from log.DianzanPO import DianzanPO
class DianzanDAO:
    def __init__(self, conn):
        self.cn = conn

    def adddianzan(self, dianzan):
        user_id = dianzan.get_user_id()
        feed_id = dianzan.get_feed_id()
        sql = "insert into dianzan(feed_id, user_id) values('%d','%d')" % (feed_id, user_id)
        try:
            # cursor = self.cn.cursor()
            self.cn.execute(sql)
            # cursor.close()
        except:
            print("insert error")


    def deletedianzan(self, id):
        sql = "delete from dianzan where dianzan_id = '%d'" % id
        try:
            # cursor = self.cn.cursor()
            self.cn.execute(sql)
            # cursor.close()
        except:
            print("delete error")

    def deletedianzan2(self, feed_id, user_id):
        sql = "delete from dianzan where feed_id = '%d'and user_id = '%d'" % (feed_id, user_id)
        try:
            # cursor = self.cn.cursor()
            self.cn.execute(sql)
            # cursor.close()
        except:
            print("delete error")

    def querydianzancount(self, feed_id):
        sql = "SELECT * FROM dianzan where feed_id = '%d'" % feed_id
        rs = self.cn.query(sql)
        user_id = []
        user_name = []
        for i in rs:
            user_id.append(i['user_id'])
        for i in user_id:
            sql = "select * from users where id = '%d'" % int(i)
            rs = self.cn.query(sql)
            if rs:
                user_name.append(rs[0]['name'])
        print(user_name)
        return user_name



