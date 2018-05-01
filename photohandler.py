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
from DataBaseManager import DataBaseManager
from PhotoPO import PhotoPO
from PhotoDAO import PhotoDAO
from basehandler import BaseHandler
d={} 
define("album_id", default=233,  type=int)
define("user_id", default=501, type=int)
class PhotosUploadHandler(BaseHandler):
    def get(self):
        #__TODO:替换为上传相片的模板html文件
        self.render("shangchuan.html")
    def fileup(self,file,path):
        upload_path=os.path.join(os.path.dirname(__file__),path)  #文件的暂存路径
        file_metas=self.request.files[file]    #提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename=meta['filename']
            filepath=os.path.join(upload_path,filename)
            with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])
        
        return(filename)
    def mkdir(self,path):  
  
        folder = os.path.exists(path)  
  
        if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹  
            os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径  
            print ("---  new folder...  ---"  )
            print ("---  OK  ---"  )
  
        else:  
            print ("---  There is this folder!  ---"  )
          
    def info_up(self,album_id,user_id,photo_name,photo_description,update_date,file_name,is_public):                                #数据插入数据库
        photo = PhotoPO()
        photo.set_album_id(album_id)
        photo.set_user_id(user_id)
        photo.set_photo_name(photo_name) 
        photo.set_photo_description(photo_description)
        photo.set_update_date(update_date)
        photo.set_file_name(file_name)
        photo.set_is_public(is_public)
        pho= PhotoDAO(self.db)
        self.write("insert!!")
        pho.addphoto(photo)
    def post(self):
        #__TODO:处理通过post方法传来的上传相片的表单
        self.set_header("Content-Type", "text/plain")
        update_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取当前时间
        album_id=self.get_body_argument("xia")#上传到哪个相册
   
        photo_name1=self.get_body_argument("nameee1") #照片名字
        photo_name2=self.get_body_argument("nameee2") 
        photo_name3=self.get_body_argument("nameee3") 
        photo_name4=self.get_body_argument("nameee4") 

        photo_description1=self.get_body_argument("description1") #照片描述
        photo_description2=self.get_body_argument("description2") 
        photo_description3=self.get_body_argument("description3") 
        photo_description4=self.get_body_argument("description4") 
#唐永剑 注释 测试
        v1=self.get_body_argument("box1")#是否上传
        v2=self.get_body_argument("box2")
        v3=self.get_body_argument("box3")
        v4=self.get_body_argument("box4")
        v_sum=v1+v2+v3+v4
        gk1=self.get_body_argument("box11") #是否公开
        gk2=self.get_body_argument("box12")
        gk3=self.get_body_argument("box13")
        gk4=self.get_body_argument("box14")
        d[0]=[update_date,album_id,photo_name1,photo_description1,v1,gk1]
        d[1]=[update_date,album_id,photo_name2,photo_description2,v2,gk2]
        d[2]=[update_date,album_id,photo_name3,photo_description3,v3,gk3]
        d[3]=[update_date,album_id,photo_name4,photo_description4,v4,gk4]
        #string='d'+str(0)+str(d[0])
        #print (string)

        file="E:\\vs\\home\\websever2\\webserver2\\web\\files"
        file_user=file+"\\yulin" 
        self.mkdir(file_user)
        #self.fileup('fk0',file_user)
        a=self.get_body_argument("fk3")
        if not a:
            print("a=Null")
        if(v1=='1'):
            filename_1=self.fileup('fk0',file_user)
            path_filename_1=file_user+"\\"+filename_1
            self.write("finished!!")
            print(path_filename_1)
            self.info_up(options.album_id,options.user_id,photo_name1,photo_description1,update_date,path_filename_1,gk1)#将信息插入数据库
        if(v2=='1'):
            filename_2=self.fileup('fk1',file_user)
            path_filename_2=file_user+"\\"+filename_2
            self.write("finished!!")
            print(path_filename_2)
            self.info_up(options.album_id,options.user_id,photo_name2,photo_description2,update_date,path_filename_2,gk2)#将信息插入数据库
        if(v3=='1'):
            filename_3=self.fileup('fk2',file_user)
            path_filename_3=file_user+"\\"+filename_3
            self.write("finished!!")
            print(path_filename_3)
            self.info_up(options.album_id,options.user_id,photo_name3,photo_description3,update_date,path_filename_3,gk3)#将信息插入数据库
        if(v4=='1'):
            filename_4=self.fileup('fk3',file_user)
            path_filename_4=file_user+"\\"+filename_4
            self.write("finished!!")
            print(path_filename_4)
            self.info_up(options.album_id,options.user_id,photo_name4,photo_description4,update_date,path_filename_4,gk4)#将信息插入数据库
        self.write("succeddful!!")

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
        '''photo=PhotoPO()
        photo.set_photo_id(photo_delete_id)
        #photo1.set_user_id()
        pho= PhotoDAO(self.db)
        self.write("delete!!")
        pho.deletephoto(photo)'''

class FeedHandler(BaseHandler):
    def get(self):
        self.write("传说中的朋友圈")