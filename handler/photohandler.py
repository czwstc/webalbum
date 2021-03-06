import bcrypt
import concurrent.futures
import MySQLdb
import os.path
import re
from PIL import Image
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
import zipfile

from log.PhotoPO import PhotoPO
from log.PhotoDAO import PhotoDAO
from basehandler import BaseHandler
from log.FeedDAO import FeedDAO
from log.FeedDAO import FeedPO


class PhotosUploadHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        uid = self.current_user.id
        albums = self.db.query("SELECT album_id,album_name FROM album WHERE user_id = %s", uid)
        self.render("shangchuan.html", albums=albums)

    def fileup(self, file, path):
        s = '..' + os.path.sep
        upload_path = os.path.join(os.path.dirname(__file__), s, path)  # 文件的暂存路径
        file_metas = self.request.files[file]  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])

        return (filename)

    def suolue(self, file, id):
        infile = file
        # outfile = 'static\\images\\min\\'+str(id)+'.jpg'
        s1 = str(id) + '.jpg'
        outfile = os.path.join('static', 'images', 'min', s1)
        print(os.path.splitext(infile)[0])
        if infile != outfile:
            try:
                im = Image.open(infile)
                print(im.size)
                height_img = int(im.size[1] * 400 / im.size[0])
                size = (400, height_img)
                print(size)
                im.thumbnail(size)
                im.save(outfile)
            except IOError:
                print("cannot create thumbnail for", infile)

    def mkdir(self, path):

        folder = os.path.exists(path)

        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("---  new folder...  ---")
            print("---  OK  ---")

        else:
            print("---  There is this folder!  ---")

    def feed_up(self, user_id, photo_id, reason, feed_time):
        feed = FeedPO()
        feed.set_photo_id(photo_id)
        feed.set_user_id(user_id)
        feed.set_time(feed_time)
        feed.set_reason(reason)
        feeddao = FeedDAO(self.db)
        feeddao.addfeed(feed)

    def info_up(self, album_id, user_id, photo_name, photo_description, update_date, file_name, is_public):  # 数据插入数据库
        photo = PhotoPO()
        photo.set_album_id(album_id)
        photo.set_user_id(user_id)
        photo.set_photo_name(photo_name)
        photo.set_photo_description(photo_description)
        photo.set_update_date(update_date)
        photo.set_file_name(file_name)
        photo.set_is_public(is_public)
        pho = PhotoDAO(self.db)
        pho.addphoto(photo)

        # 服务于feed, 给出photo_id

        sql = 'SELECT photo_id FROM photo ORDER BY photo_id DESC LIMIT 1'
        print(self.db.query(sql))
        return self.db.query(sql)

    @tornado.web.authenticated
    def post(self):
        d = {}

        update_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当前时间
        user_id = self.current_user.id
        album_id = int(self.get_body_argument("xia"))  # 上传到哪个相册

        photo_name1 = self.get_body_argument("nameee1")  # 照片名字
        photo_name2 = self.get_body_argument("nameee2")
        photo_name3 = self.get_body_argument("nameee3")
        photo_name4 = self.get_body_argument("nameee4")

        photo_description1 = self.get_body_argument("description1")  # 照片描述
        photo_description2 = self.get_body_argument("description2")
        photo_description3 = self.get_body_argument("description3")
        photo_description4 = self.get_body_argument("description4")

        v1 = self.get_body_argument("box1")  # 是否上传
        v2 = self.get_body_argument("box2")
        v3 = self.get_body_argument("box3")
        v4 = self.get_body_argument("box4")
        v_sum = v1 + v2 + v3 + v4
        gk1 = self.get_body_argument("box11")  # 是否公开
        gk2 = self.get_body_argument("box12")
        gk3 = self.get_body_argument("box13")
        gk4 = self.get_body_argument("box14")
        d[0] = [update_date, album_id, photo_name1, photo_description1, v1, gk1]
        d[1] = [update_date, album_id, photo_name2, photo_description2, v2, gk2]
        d[2] = [update_date, album_id, photo_name3, photo_description3, v3, gk3]
        d[3] = [update_date, album_id, photo_name4, photo_description4, v4, gk4]
        # file="static\\\\images"
        # file_user=file
        file = os.path.join('static', 'images')
        file_user = file
        file_suolue = os.path.join(file, 'min')
        self.mkdir(file)
        if (v1 == '1'):
            filename_1 = self.fileup('fk0', file_user)  # 上传到static\\images
            path_filename_1 = file_user + os.path.sep + filename_1
            print(path_filename_1)
            if self.get_argument("box11") == '1':
                feed_photo_id = self.info_up(album_id, user_id, photo_name1, photo_description1, update_date,
                                             filename_1,
                                             gk1)  # 将信息插入数据库
                self.feed_up(user_id, feed_photo_id[0]['photo_id'], photo_description1, update_date)
            else:
                self.info_up(album_id, user_id, photo_name1, photo_description1, update_date,
                             filename_1,
                             gk1)  # 将信息插入数据库
            al = self.db.query("SELECT photo_id FROM photo WHERE file_name ='%s' " % (filename_1))
            print("al=", al[-1]['photo_id'])  # 返回的是一个列表里面的嵌入字典，打印最下面的一行的photo_id
            self.suolue(path_filename_1, al[-1]['photo_id'])

            self.db.execute("UPDATE album SET cover_id = '%s'WHERE album_id ='%s' " % (al[-1]['photo_id'], album_id))

        if (v2 == '1'):
            filename_2 = self.fileup('fk1', file_user)
            path_filename_2 = file_user + os.path.sep + filename_2
            print(path_filename_2)
            if self.get_argument("box12") == '1':
                feed_photo_id = self.info_up(album_id, user_id, photo_name2, photo_description2, update_date,
                                             filename_2, gk2)  # 将信息插入数据库
                self.feed_up(user_id, feed_photo_id[0]['photo_id'], photo_description2, update_date)
            else:
                self.info_up(album_id, user_id, photo_name2, photo_description2, update_date, filename_2,
                             gk2)  # 将信息插入数据库
            al = self.db.query("SELECT photo_id FROM photo WHERE file_name ='%s' " % (filename_2))
            print("al=", al[-1]['photo_id'])  # 返回的是一个列表里面的嵌入字典，打印最下面的一行的photo_id
            self.suolue(path_filename_2, al[-1]['photo_id'])

            self.db.execute("UPDATE album SET cover_id = '%s'WHERE album_id ='%s' " % (al[-1]['photo_id'], album_id))

        if (v3 == '1'):
            filename_3 = self.fileup('fk2', file_user)
            path_filename_3 = file_user + os.path.sep + filename_3
            print(path_filename_3)
            if self.get_argument("box13") == '1':
                feed_photo_id = self.info_up(album_id, user_id, photo_name3, photo_description3, update_date,
                                             filename_3, gk3)  # 将信息插入数据库
                self.feed_up(user_id, feed_photo_id[0]['photo_id'], photo_description3, update_date)
            else:
                self.info_up(album_id, user_id, photo_name3, photo_description3, update_date, filename_3,
                             gk3)  # 将信息插入数据库
            al = self.db.query("SELECT photo_id FROM photo WHERE file_name ='%s' " % (filename_3))
            print("al=", al[-1]['photo_id'])  # 返回的是一个列表里面的嵌入字典，打印最下面的一行的photo_id
            self.suolue(path_filename_3, al[-1]['photo_id'])

            self.db.execute("UPDATE album SET cover_id = '%s'WHERE album_id ='%s' " % (al[-1]['photo_id'], album_id))

        if (v4 == '1'):
            filename_4 = self.fileup('fk3', file_user)
            path_filename_4 = file_user + os.path.sep + filename_4
            print(path_filename_4)
            if self.get_argument("box14") == '1':
                feed_photo_id = self.info_up(album_id, user_id, photo_name4, photo_description4, update_date,
                                             filename_4, gk4)  # 将信息插入数据库
                self.feed_up(user_id, feed_photo_id[0]['photo_id'], photo_description4, update_date)
            else:
                self.info_up(album_id, user_id, photo_name4, photo_description4, update_date,
                             filename_4, gk4)  # 将信息插入数据库
            al = self.db.query("SELECT photo_id FROM photo WHERE file_name ='%s' " % (filename_4))
            print("al=", al[-1]['photo_id'])  # 返回的是一个列表里面的嵌入字典，打印最下面的一行的photo_id
            self.suolue(path_filename_4, al[-1]['photo_id'])

            self.db.execute("UPDATE album SET cover_id = '%s'WHERE album_id ='%s' " % (al[-1]['photo_id'], album_id))

        sum = int(v1) + int(v2) + int(v3) + int(v4)
        self.db.execute("UPDATE album SET edit_date = '%s'WHERE album_id ='%s' " % (update_date, album_id))
        albumname = self.db.query("SELECT album_name FROM album WHERE album_id ='%d' " % (album_id))
        self.render("successful_upload.html", sum=sum, albumname=albumname[0]['album_name'])


class PhotoHandler(BaseHandler):
    def get(self, uid, albumid, photoid):
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            route = list(self.db.query("SELECT * FROM photo WHERE user_id = %s and album_id =%s", uid, albumid))
        #    self.write(str(route))

        # route=list()
        # route=["/static/img/homebg.jpg","/static/img/roll.jpg","/static/images/min/1.jpg"]
        self.render("PhotoListHandler.html", route=route)


class PhotoPlayHandler(BaseHandler):
    def get(self, uid, albumid):
        pass


class PhotosListHandler(BaseHandler):
    def get(self, uid, albumid):
        album = self.db.get("SELECT * FROM album WHERE album_id = %s", albumid)
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            photo = self.db.query("SELECT * FROM photo WHERE album_id = %s AND user_id = %s", albumid, uid)
            self.render("photos_show.html", user=user, photos=photo, album=album)


class Photosall(BaseHandler):
    def get(self, uid):
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        album = self.db.query("SELECT * FROM album WHERE user_id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            photo = self.db.query("SELECT * FROM photo WHERE user_id = %s ", user.id)
            self.render("photosall.html", user=user, photos=photo)


class PhotoDeleteHandler(BaseHandler):
    def get(self, uid, albumid, photoid):
        self.db.execute("DELETE FROM photo WHERE photo_id = %s", photoid)
        try:
            self.db.execute("delete from feed where photo_id = %d", int(photoid))
        except:
            pass
        # self.write("相片删除页面，用户id,相册id，相片id分别为" + str(uid) + " " + str(albumid) + " " + str(photoid))
        album = self.db.get("SELECT * FROM album WHERE album_id = %s", albumid)
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            photo = self.db.query("SELECT * FROM photo WHERE album_id = %s AND user_id = %s", albumid, uid)
            self.render("photos_show.html", user=user, photos=photo, album=album)

    def post(self):
        pass


class jc_PhotoPlayHandler(BaseHandler):
    def get(self):
        album_id = '1'
        try:
            photo = self.db.query("select * from photo where album_id = '%d'", int(album_id))
        except:
            pass
        self.render("carousel.html")

    def post(self):
        pass

class PhotosDownloadHandler(BaseHandler):
    def get(self,uid,album_id):
        print("downloading..album_id : "+album_id)
        file_list=[]
        files=self.db.query("SELECT * FROM photo WHERE album_id = %s",album_id)

        s = os.path.pardir + os.path.sep + 'static'+ os.path.sep+ 'images'+ os.path.sep

        for file in files:
            upload_path = os.path.join(os.path.dirname(__file__), s, file.file_name)
            file_list.append(upload_path) 

        print(file_list)

        zip_file_name="a"+album_id+".zip"
        zip_file = s + zip_file_name
        zip_file = os.path.join(os.path.dirname(__file__),zip_file)
        self.zip_files(file_list, zip_file)

        with open( zip_file, "rb") as f:
            self.set_header('Content-Type','application/octet-stream')
            self.set_header ('Content-Disposition', 'attachment; filename='+zip_file_name)
            self.write(f.read())


    def zip_files(self, files, zip_name ):
        zip = zipfile.ZipFile( zip_name, 'w', zipfile.ZIP_DEFLATED )
        for file in files:
            print ('compressing', file)
            zip.write( file )
        zip.close()
        print ('compressing finished')

class PhotoDeleteHandler(BaseHandler):
    def get(self, uid, albumid, photoid):
        self.db.execute("DELETE FROM photo WHERE photo_id = %s", photoid)
        #self.write("相片删除页面，用户id,相册id，相片id分别为" + str(uid) + " " + str(albumid) + " " + str(photoid))
        album = self.db.get("SELECT * FROM album WHERE album_id = %s", albumid)
        user = self.db.get("SELECT * FROM users WHERE id = %s", uid)
        if not user:
            raise tornado.web.HTTPError(404)
        else:
            photo = self.db.query("SELECT * FROM photo WHERE album_id = %s AND user_id = %s", albumid, uid)
            self.render("photos_show.html", user=user, photos=photo, album=album)

    def post(self):
        pass


class jc_PhotoPlayHandler(BaseHandler):
    def get(self):
        self.render("carousel.html")

    def post(self):
        pass

class PhotoDownloadHandler(BaseHandler):
    def get(self,uid,album_id,photo_id):
        print("downloading..photo_id : "+photo_id)
        file=self.db.get("SELECT * FROM photo WHERE photo_id = %s",photo_id)

        s = os.path.pardir + os.path.sep + 'static'+ os.path.sep+ 'images'+ os.path.sep
        upload_path = os.path.join(os.path.dirname(__file__), s, file.file_name)

        print(upload_path)

        with open( upload_path, "rb") as f:
            self.set_header('Content-Type','application/octet-stream')
            self.set_header ('Content-Disposition', 'attachment; filename='+file.file_name)
            self.write(f.read())