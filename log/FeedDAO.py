import time
from log.FeedPO import FeedPO


class FeedDAO:
    def __init__(self, conn):
        self.cn = conn

    def adddfeed(self, feed):
        photo_id = feed.get_photo_id()
        user_id = feed.get_user_id()
        reason = feed.get_reason()
        sql = "insert into feed(photo_id, user_id, reason, time) values('%d','%d','%s','%s')" % (
            photo_id, user_id, reason, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        try:
            # cursor = self.cn.cursor()
            self.cn.execute(sql)
            # cursor.close()
        except:
            print("insert error")

    def deletefeed(self, id):
        sql = "delete from feed where feed_id = '%d'" % id
        try:
            # cursor = self.cn.cursor()
            self.cn.execute(sql)
            # cursor.close()
        except:
            print("delete error")

    def queryfeeds(self):
        feed = []
        feed_comment = []
        feed_dianzan = []
        feed_photo = []
        sql = "select jcuser.user_name, feed.* from jcuser,feed where jcuser.user_id = feed.user_id order by feed.time"
        feed = self.cn.query(sql)
        for i in feed:
            sql = "select * from comment where feed_id = '%d'" % i['feed_id']
            commnet_rs = self.cn.query(sql)
            feed_comment.append(commnet_rs)
            sql = "select * from dianzan where feed_id = '%d'" % i['feed_id']
            dianzan_rs = self.cn.query(sql)
            feed_dianzan.append(dianzan_rs)
            sql = "select file_name from photo where photo_id = '%d'" % i['photo_id']
            photo_rs = self.cn.query(sql)
            feed_photo = feed_photo + photo_rs

        return feed, feed_comment, feed_dianzan,feed_photo




