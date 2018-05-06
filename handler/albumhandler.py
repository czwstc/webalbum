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

from log.albumPO import albumPO
from log.albumDAO import albumDAO

from basehandler import BaseHandler

class AlbumsListHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,uid):
        self.render("AlbumCreate.html")
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            album = self.db.query("SELECT * FROM album WHERE user_id = %s", uid)
            self.render("albums.html",user=user,albums=album)
        


class AlbumCreateHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
<<<<<<< HEAD
        
=======
>>>>>>> 985682e204e183aa21a8f45213d99e71007b881c
        self.render("AlbumCreate.html")

    @tornado.web.authenticated
    def post(self):
        user_id=self.get_current_user
        name=self.get_body_argument("name")
        discription=self.get_body_argument("discribe")
        now_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("name:"+name)
        print("discription:"+discription)

        album = albumPO()
        album.set_album_name(self.get_body_argument("name"))
        album.set_album_description(self.get_body_argument("discribe"))
        album.set_cover_id(0)
        album.set_user_id(int(self.current_user.id))
        album.set_create_date(now_date)
        album.set_edit_date(now_date)
        alb = albumDAO(self.db)
        alb.addalbum(album)

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
