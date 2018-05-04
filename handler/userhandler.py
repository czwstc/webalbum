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
from tornado.options import define, options
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import shutil
import time
import unicodedata
import uimodules
import pymysql
#from DataBaseManager import DataBaseManager

from basehandler import BaseHandler


class AuthCreateHandler(BaseHandler):
    def get(self):
        self.render("create_author.html")
    username="feng"
    @gen.coroutine
    def post(self):    #提交表单，上传数据库
        # if self.any_author_exists():
        #    raise tornado.web.HTTPError(400, "author already created")
        #hashed_password = yield executor.submit(
        #    bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
        #    bcrypt.gensalt())
        author_id = self.db.execute(
            "INSERT INTO users (email, name, hashed_password) "
            "VALUES (%s, %s, %s)",
            self.get_argument("email"), self.get_argument("name"),
            self.get_argument("password"))
        self.set_secure_cookie("cur_user", str(author_id))
        self.redirect(self.get_argument("next", "/"))


class AuthLoginHandler(BaseHandler):
    def get(self):
        # If there are no authors, redirect to the account creation page.
        if not self.any_author_exists():
            #self.redirect("/auth/create")
            self.render("login.html", error=None)    #临时
            self.render("module-navbar",username=username)    #导航栏要用的username
        else:
            self.render("login.html", error=None)
            self.render("module-navbar",username=username)
        

    @gen.coroutine

    
    def post(self):
        author = self.db.get("SELECT * FROM users WHERE email = %s",
                             self.get_argument("email"))
        username = self.db.get("SELECT name FROM users WHERE email = %s",    #去数据库里用email找用户名
                             self.get_argument("email"))
        if not author:
            self.render("login.html", error="email not found")
            return
        hashed_password =self.get_argument("password")
        #hashed_password = yield executor.submit(
        #   bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
        #    tornado.escape.utf8(author.hashed_password))
        if hashed_password == author.hashed_password:
            self.set_secure_cookie("cur_user", str(author.id))    #demo里面是blogdemo_user，这里要改
            self.redirect(self.get_argument("next", "/"))
        else:
            self.render("login.html", error="incorrect password")


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("blogdemo_user")
        self.redirect(self.get_argument("next", "/"))



class UserDeleteHandler(BaseHandler):
    def get(self):
        self.write("用户删除")

    @gen.coroutine
    def post(self):
        pass

class ProfileHandler(BaseHandler):
    def get(self,uid):
        self.write("id:" + str(uid)+" 个人资料展示页面")


class ProfileEditHandler(BaseHandler):
    def get(self,uid):
        self.write("id:" +str(uid)+" 个人资料编辑")

    @gen.coroutine
    def post(self,uid):
        pass
