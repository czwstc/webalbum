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

from basehandler import BaseHandler


class FeedHandler(BaseHandler):
    def get(self):
        entries = []
        feeddao = FeedDAO(self.db)
        feed, feed_c, feed_d, feed_p = feeddao.queryfeeds()
        print(feed_p)
        self.render("feed.html", feed=feed, feed_c=feed_c, feed_d=feed_d, feed_p=feed_p)
