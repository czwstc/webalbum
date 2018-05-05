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
    def get(self):
        entries = []
        feeddao = FeedDAO(self.db)
        feed, feed_c, feed_d, feed_p = feeddao.queryfeeds()
        self.render("feed.html", feed=feed, feed_c=feed_c, feed_d=feed_d, feed_p=feed_p)

    def post(self):
        dianzandao = DianzanDAO(self.db)
        dianzan = DianzanPO()
        d_feed_id = self.get_argument("name", None)
        if self.get_argument("color", None) == 'white':
            dianzan.set_feed_id(int(d_feed_id))
            dianzan.set_user_id(1)
            dianzandao.adddianzan(dianzan)
            print("成功添加")
        else:
            dianzandao.deletedianzan2(int(d_feed_id), 1)
            print("成功删除")
        num = dianzandao.querydianzancount(int(d_feed_id))
        data = {'status': 0, 'message': 'successfully', 'data': num}  # 封装数据
        self.write(json.dumps(data))

