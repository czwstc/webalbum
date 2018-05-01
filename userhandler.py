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

from basehandler import BaseHandler


class UserCreateHandler(BaseHandler):
    def get(self):
        self.write("用户注册")

    @gen.coroutine
    def post(self):
        pass


class UserLoginHandler(BaseHandler):
    def get(self):
        self.set_secure_cookie("cur_user", "1")

    @gen.coroutine
    def post(self):
        pass


class UserLogoutHandler(BaseHandler):
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
    def get(self,uid):
        self.write("id:" + str(uid)+" 个人资料展示页面")


class ProfileEditHandler(BaseHandler):
    def get(self,uid):
        self.write("id:" +str(uid)+" 个人资料编辑")

    @gen.coroutine
    def post(self,uid):
        pass