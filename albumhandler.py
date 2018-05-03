import bcrypt
import concurrent.futures
import MySQLdb
import os.path
import re
import subprocess
import torndb
import tornado.escape
import time
from tornado import gen
from tornado.web import url
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import uimodules

import pymysql
from DataBaseManager import DataBaseManager
from albumPO import albumPO
from albumDAO import albumDAO

from basehandler import BaseHandler

Host='47.104.68.55'
Port=3306
User='root'
Passwd='linux'
DB='test'
Charset='utf8'

#conn = pymysql.Connect(
#    host=Host,
#    port=Port,
#    user=User,
#    passwd=Passwd,
#    db=DB,
#    charset=Charset
#)



db={}
class AlbumsListHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,uid):
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            album = self.db.query("SELECT * FROM album WHERE user_id = %s", uid)
            if not album:
                self.redirect("/albums/new")
            else:
                self.render("albums.html",user=user,albums=album)
        


class AlbumCreateHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        #__TODO:替换为创建相册的模板html文件
        self.render("AlbumCreate.html")
    @tornado.web.authenticated
    def post(self):
        #__TODO:处理通过post方法传来的创建相册的表单
        self.set_header("Content-Type", "text/plain")
        user_id=self.get_current_user
        length1=len(db)+1
        name=self.get_body_argument("name")
        discription=self.get_body_argument("discribe")
        now_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db[length1]= [name,discription] 
        print("name:"+name)
        print("discription:"+discription)
        print(db)
        print(length1)

        album = albumPO()
        album.set_album_name(self.get_body_argument("name"))
        album.set_album_description(self.get_body_argument("discribe"))
        album.set_cover_id(1)
        album.set_user_id(int(self.current_user.id))
        album.set_create_date(now_date)
        album.set_edit_date(now_date)
        alb = albumDAO(self.db)
        alb.addalbum(album)

        #self.db.commit()
        #self.db.close()

        user_id=self.get_current_user
        self.redirect("/u/"+str(self.current_user.id)+"/albums")

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

class MyAlbumsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_id=self.get_current_user
        self.redirect("/u/"+str(self.current_user.id)+"/albums")
