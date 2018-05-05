
import time
from log.CommentPO import CommentPO


class CommentDAO:
    def __init__(self, conn):
        self.cn = conn

    def addcomment(self, comment):
        photo_id = comment.get_photo_id()
        user_id = comment.get_user_id()
        feed_id = comment.get_feed_id()
        comment_body = comment.get_comment_body()
        sql = "insert into comment(feed_id, photo_id, user_id, comment_body,time) values('%d','%d','%d','%s','%s')" % (feed_id, photo_id, user_id, comment_body, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        try:
            #cursor = self.cn.cursor()
            self.cn.execute(sql)
            #cursor.close()
        except:
            print("insert error")


    def deletecomment(self, comment_id):
        try:
            sql = "delete from comment where comment_id = '%d'" % comment_id
            # cursor = self.cn.cursor()
            self.cn.execute(sql)
            # cursor.close()
        except:
            print("delete error")

    def updatecomment(self, comment):
        id = comment.get_id()
        comment_body = comment.get_comment_body()
        sql = "update comment set comment_body = '%s',time = '%s' where comment_id = '%d'" % (comment_body, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), id)
        try:
            # cursor = self.cn.cursor()
            self.cn.execute(sql)
            # cursor.close()
        except:
            print("insert error")

    def queryCommentByFeedId(self, feed_id):
        comment_body = []
        user_id = []
        try:
            sql = "SELECT * FROM comment where feed_id = '%d'" % feed_id
            rs = self.cn.query(sql)
            for i in rs:
                comment_body.append(i['comment_body'])
                user_id.append(i['user_id'])
        except:
            print("query error")
        return comment_body, user_id


    def queryCommentByPhoto_ids(self, photo_id):
        mylist = []
        for i in photo_id:
            try:
                sql = "SELECT * FROM comment where photo_id = '%d'" % i
                rs = self.cn.query(sql)
                mylist.append(rs)
            except:
                print("query error")
        return mylist
