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
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            albums = self.db.query("SELECT * FROM album WHERE user_id = %s", uid)
            photos_num={}
            for album in albums:
                photos = self.db.get("SELECT COUNT(*) AS NUM FROM photo WHERE album_id = %s", album.album_id)
                photos_num[album.album_id]=int(photos.NUM)
            self.render("albums.html",user=user,albums=albums,photos_num=photos_num)
            
        


class AlbumCreateHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
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

        #self.redirect("/u/"+str(self.current_user.id)+"/albums")
        self.render("SuccessfulNewAlbum.html")

class AlbumEditHandler(BaseHandler):
    def post(self):
        album_id=self.get_body_argument("album_id")
        name=self.get_body_argument("name")
        discription=self.get_body_argument("discribe")
        now_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


        self.db.execute("UPDATE album SET album_name=name,album_description=discription,edit_date=now_date WHERE album_id = %s",album_id)

        

class AlbumDeleteHandler(BaseHandler):
    def post(self):
        user=self.current_user
        album_id=self.get_body_argument("album_id")
        self.db.execute("DELETE FROM album WHERE album_id = %s",album_id)
        self.db.execute("DELETE FROM photo WHERE album_id = %s",album_id)
        self.redirect("/u/"+str(self.current_user.id)+"/albums")

class MyAlbumsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_id=self.get_current_user
        self.redirect("/u/"+str(self.current_user.id)+"/albums")
