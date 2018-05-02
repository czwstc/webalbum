import time
from log.DianzanPO import DianzanPO
class DianzanDAO:
    def __init__(self, conn):
        self.cn = conn

    def adddianzan(self, dianzan):
        photo_id = dianzan.get_photo_id()
        user_id = dianzan.get_user_id()
        feed_id = dianzan.get_feed_id()
        sql = "insert into dianzan(feed_id, photo_id, user_id,time) values('%d', '%d','%d','%s')" % (feed_id, photo_id, user_id, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
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


    def querydianzanByPhoto(self, comment):
        l = []
        photo_id = comment.get_photo_id()
        user_id = comment.get_user_id()
        sql = "SELECT * FROM comment where photo_id = '%d', user_id = '%d'" % (photo_id, user_id)
        try:
            rs = self.cn.query.fetchall()
            for dianzan in rs:
                dianzan = DianzanPO()
                dianzan.set_photo_id(dianzan[0])
                dianzan.set_user_id(dianzan[1])
                dianzan.set_time(dianzan[2])
                l.append(dianzan)
        except:
            print("query error")
        return l


