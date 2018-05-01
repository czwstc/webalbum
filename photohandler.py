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

class PhotosUploadHandler(BaseHandler):
    def get(self):
        #__TODO:替换为上传相片的模板html文件
        self.render("xxxx.html")

    def post(self):
        #__TODO:处理通过post方法传来的上传相片的表单
        pass

class PhotoHandler(BaseHandler):
    def get(self,uid,albumid,photoid):
        self.write("单个相片页面，用户id,相册id，相片id分别为"+str(uid)+" "+str(albumid)+" "+str(photoid))

class PhotosListHandler(BaseHandler):
    def get(self,uid,albumid):
        self.write("相册中相片列表，用户id,相册id分别为"+str(uid)+" "+str(albumid))

class PhotoDeleteHandler(BaseHandler):
    def get(self,uid,albumid,photoid):
        self.write("相片删除页面，用户id,相册id，相片id分别为"+str(uid)+" "+str(albumid)+" "+str(photoid))
    def post(self):
        pass

class FeedHandler(BaseHandler):
    def get(self):
        self.write("传说中的朋友圈")