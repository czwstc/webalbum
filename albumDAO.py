import pymysql
from albumPO import albumPO
from DataBaseManager import DataBaseManager

class albumDAO:
    def __init__(self, conn):
        self.cn = conn

    def addalbum(self, album):
        album_id = album.get_album_id()
        album_name = album.get_album_name()
        album_description = album.get_album_description()
        cover_id = album.get_cover_id()
        user_id = album.get_user_id()
        create_date = album.get_create_date()
        edit_date = album.get_edit_date()
        sql = "insert into album(album_id, album_name, album_description,cover_id,user_id,create_date,edit_date) values('%s','%s','%s','%s','%s','%s','%s')" % (album_id, album_name, album_description,cover_id,user_id,create_date,edit_date)
        try:
            cursor = self.cn.cursor()
            cursor.execute(sql)
            cursor.close()
        except:
            print("insert error")


    def deletealbum(self, albums):
        sql = ''
        try:   
            cursor = self.cn.cursor()
            cursor.execute(sql)
            cursor.close()
        except:
            print("delete error")

    def updatealbum(self, album):
        album_description = album.get_album_description()
        cover_id = album.get_cover_id()
        edit_date = album.get_edit_date()
        sql = "update albums set album_description = '%s' cover_id = '%s' edit_date = '%s'" % (album_description, cover_id, edit_date)
        try:
            cursor = self.cn.cursor()
            cursor.execute(sql)
            cursor.close()
        except:
            print("updata error")

    def queryalbum(self, album_id):
        l = []
        try:
            sql = "SELECT * FROM albums where album_id = '%s'" % album_id
            cursor = self.cn.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            for album in rs:
                myalbum = albumPO()
                myalbum.set_album_id(album[0])
                myalbum.set_album_name(album[1])
                myalbum.set_album_description(album[2])
                myalbum.set_cover_id(album[3])
                myalbum.set_user_id(album[4])
                myalbum.set_create_date(album[5])
                myalbum.set_edit_date(album[6])
                if myalbum.get_album_id() == album_id:
                    l.append(myalbum)
            cursor.close()
        except:
            print("query error")
        return l

