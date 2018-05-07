import bcrypt
import concurrent.futures
import MySQLdb
import os.path
import re
import subprocess
import torndb
import tornado.escape
from tornado import gen
from tornado.web import url
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import uimodules
from log.DianzanDAO import DianzanDAO
from log.DianzanDAO import DianzanPO
from log.CommentDAO import CommentDAO
from log.CommentDAO import CommentPO
from log.FeedDAO import FeedPO
from log.FeedDAO import FeedDAO
import simplejson as json

from basehandler import BaseHandler


class FeedHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        entries = []
        feeddao = FeedDAO(self.db)
        feed, feed_c, feed_d, feed_p = feeddao.queryfeeds()
        if self.get_current_user():
            user_id = self.get_current_user().id
        else:
            user_id = -1
        like_flag = []
        for i in range(len(feed)):
            for j in feed_d[i]:
                if j['user_id'] == user_id:
                    like_flag.append(1)
                    break
                like_flag.append(0)
        self.render("feed.html", feed=feed, feed_c=feed_c, feed_d=feed_d, feed_p=feed_p, like_flag=like_flag, user_id=user_id, user=self.current_user)

    #@tornado.web.authenticated
    def post(self):
        #print(self.get_current_user())
        #if self.get_current_user() is None:
            #print(1)
           # self.redirect("login.html")
        #else:
            # 点赞部分处理
            dianzandao = DianzanDAO(self.db)
            dianzan = DianzanPO()
            d_feed_id = self.get_argument("name", None)
            if d_feed_id:
                if self.get_argument("background", None) == 'gray':
                    dianzan.set_feed_id(int(d_feed_id))
                    dianzan.set_user_id(self.get_current_user().id)
                    dianzandao.adddianzan(dianzan)
                    print("成功添加")
                else:
                    dianzandao.deletedianzan2(int(d_feed_id), self.get_current_user().id)
                    print("成功删除")
                num = dianzandao.querydianzancount(int(d_feed_id))
                data = {'status': 0, 'message': 'successfully', 'data': num}  # 封装数据
                self.write(json.dumps(data))

            # 评论部分处理
            commentdao = CommentDAO(self.db)
            comment = CommentPO()
            p_feed_id = self.get_argument("p_feed_id", None)
            c_feed_id = self.get_argument("c_feed_id", None)
            comment_body = self.get_argument("comment_body", None)
            if comment_body:
                comment.set_user_id(self.get_current_user().id)
                comment.set_feed_id(int(c_feed_id))
                comment.set_photo_id(int(p_feed_id))
                comment.set_comment_body(comment_body)
                commentdao.addcomment(comment)
                comment_bodys, user_ids = commentdao.queryCommentByFeedId(int(c_feed_id))
                data = {'status': 0, 'message': 'successfully', 'comment_bodys': comment_bodys,
                        'user_name': self.get_current_user().name}  # 封装数据
                self.write(json.dumps(data))






