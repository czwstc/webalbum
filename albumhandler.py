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

class AlbumsListHandler(BaseHandler):
    def get(self,uid):
    #数据库端未建立，暂时用一个测试用的数据作为返回数据
        test = dict(
            album_id=1,
            album_name="超哥的小时候",
            album_description="一些小学初中大学的照片~",
            cover_id=1,
            user_id=uid,
            create_date="20180422",
            edit_date="20180422"
        )
        self.render("albums.html",albums=test)


class AlbumCreateHandler(BaseHandler):
    def get(self):
        #__TODO:替换为创建相册的模板html文件
        self.render("xxxx.html")

    def post(self):
        #__TODO:处理通过post方法传来的创建相册的表单
        pass

class AlbumEditHandler(BaseHandler):
    def get(self,uid,albumid):
        self.write("相册编辑，用户id和相册id分别为"+str(uid)+" "+str(albumid))

    def post(self):
        pass

class AlbumDeleteHandler(BaseHandler):
    def get(self,uid,albumid):
         self.write("相册删除，用户id和相册id分别为"+str(uid)+" "+str(albumid))

    def post(self):
        pass