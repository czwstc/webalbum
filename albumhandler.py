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

conn = pymysql.Connect(
    host=Host,
    port=Port,
    user=User,
    passwd=Passwd,
    db=DB,
    charset=Charset
)



db={}
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
        self.render("AlbumCreate.html")

    def post(self):
        #__TODO:处理通过post方法传来的创建相册的表单
        self.set_header("Content-Type", "text/plain")
        length1=len(db)+1
        name=self.get_body_argument("name")
        discription=self.get_body_argument("discribe")
        db[length1]= [name,discription] 
        print("name:"+name)
        print("discription:"+discription)
        print(db)
        print(length1)

        album = albumPO()
        album.set_album_id('12232') 
        album.set_album_name(self.get_body_argument("name"))
        album.set_album_description(self.get_body_argument("discribe"))
        album.set_cover_id('369')
        album.set_user_id('111')
        album.set_create_date('429')
        album.set_edit_date('429')
        alb = albumDAO(conn)
        alb.addalbum(album)

        conn.commit()
        conn.close()

        self.write("success!")

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