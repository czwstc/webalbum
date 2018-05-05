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
    @gen.coroutine
    def post(self):    #提交表单，上传数据库
        # if self.any_author_exists():
        #    raise tornado.web.HTTPError(400, "author already created")
        #hashed_password = yield executor.submit(
        #    bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
        #    bcrypt.gensalt())
        author_id = self.db.execute(
            "INSERT INTO users (email, name, hashed_password,nickname,user_description) "
            "VALUES (%s, %s, %s,%s,%s)",
            self.get_argument("email"), self.get_argument("name"),
            self.get_argument("password"), self.get_argument("nickname"),
            self.get_argument("user_description"))
        self.set_secure_cookie("cur_user", str(author_id))
        self.redirect(self.get_argument("next", "/"))


class AuthLoginHandler(BaseHandler):
    def get(self):
        # If there are no authors, redirect to the account creation page.
        if self.get_current_user():
            username=self.get_current_user().name
        else:
            username="未登录"
        if not self.any_author_exists():
            self.render("login.html", error=None,username=username)    #临时
        else:
            self.render("login.html", error=None,username=username)    #临时
                
    @gen.coroutine

    
    def post(self):
        author = self.db.get("SELECT * FROM users WHERE email = %s",
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
            self.redirect(self.get_argument("next", "/login"))
        else:
            self.render("login.html", error="incorrect password",username="未登录")


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("cur_user")
        self.redirect(self.get_argument("next", "/"))



class UserDeleteHandler(BaseHandler):
    def get(self):
        self.write("用户删除")

    @gen.coroutine
    def post(self):
        pass

class ProfileHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            username=self.get_current_user().name
            user_description=self.get_current_user().user_description
        else:
            username="未登录"
            user_description="这个用户很懒，什么也没有留下"
        if not user_description:
            user_description="这个用户很懒，什么也没有留下"
        self.render("pro.html",username=username,user_description=user_description)


class ProfileEditHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            username=self.get_current_user().name
            self.render("proedit.html",username=username)
        else:
            self.render("login.html")    #已登录的可以修改，没登陆的先去登录
    @gen.coroutine
    def post(self):
        if self.get_current_user():
            id=self.get_current_user().id
            user_description=self.get_argument("user_description")
        
        
        sql="UPDATE users SET user_description = '%s' WHERE id = '%s'" % (user_description,id)
        self.db.execute(sql)
        