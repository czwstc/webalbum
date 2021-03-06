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
#import uimodules    #互相import怕出问题

class BaseHandler(tornado.web.RequestHandler):
    @property    #只读属性
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("cur_user")
        if not user_id:
            return None
        return self.db.get("SELECT * FROM users WHERE id = %s", int(user_id))
    
    

    def any_author_exists(self):
        return bool(self.db.get("SELECT * FROM users LIMIT 1"))