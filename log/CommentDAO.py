
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

    def queryCommentByPhoto(self, feed_id):
        l = []
        try:
            sql = "SELECT * FROM comment where feed_id = '%d'" % feed_id
            rs = self.cn.query(sql)
            for comment in rs:
                mycomment = CommentPO()
                mycomment.set_id(comment['_Id'])
                mycomment.set_photo_id(comment['photo_id'])
                mycomment.set_user_id(comment['user_id'])
                mycomment.set_comment_body(comment['comment_body'])
                mycomment.set_time(comment['time'])
                l.append(mycomment)
        except:
            print("query error")
        return l


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
