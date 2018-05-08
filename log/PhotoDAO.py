from log.PhotoPO import PhotoPO

class PhotoDAO:
    def __init__(self, conn):
        self.cn = conn

    def addphoto(self,photo):
        photo_name = photo.get_photo_name()
        update_date = photo.get_update_date()
        album_id = photo.get_album_id()
        user_id = photo.get_user_id()
        photo_description = photo.get_photo_description()
        is_public = photo.get_is_public()
        file_name = photo.get_file_name()
        sql = "insert into photo(album_id,user_id,photo_name,photo_description,update_date,file_name,is_public) values('%d','%d','%s','%s','%s','%s','%s')"% (album_id,user_id,photo_name,photo_description,update_date,file_name,is_public) 
        try:
            self.cn.execute(sql)
        except:
            print("insert error")


    def deletephoto(self, photo):
        photo_id=photo.get_photo_id()
        try:
            sql = "delete from photo where photo_id = 's'" % (photo_id)
            self.cn.execute(sql)
        except:
            print("delete error")
    def updatephoto(self,photo):
        photo_description = photo.get_photo_description()
        photo_name = photo.get_photo_name()
        update_date = photo.get_update_date()
        is_public=photo.get_is_public()
        sql = "update photo set photo_description = '%s' photo_name = '%s' update_date = '%s' is_public = '%s'" % (photo_description, photo_name, update_date,is_public)
        try:
            self.cn.execute(sql)
        except:
            print("updata error")
    def getlastid(self):
        sql = "select top 1  from photo order by photo_id desc"
        try:
            self.cn.execute(sql)
            lastid = self.cn.query(sql)
        except:
            print("updata error")
        return lastid

    def querypublicPhoto(self):
        l_photoid=[]
        l_userid=[]
        l_time=[]
        d_transfer={}
        try:
            sql = "SELECT * FROM photo where is_public = '1' order by update_date desc" 
            rs = self.cn.query(sql)
            for photo in rs:
                photo_transfer=PhotoPO.PhotoPO()
                photo_transfer.set_photo_id(photo['photo_id'])
                photo_transfer.set_user_id(photo['user_id'])
                l_photoid.append(photo_transfer.photo_id)
                l_userid.append(photo_transfer.user_id)
                l_time.append(photo_transfer.update_date)
        except:
            print("query error")
        d_transfer[0]=l_photoid
        d_transfer[1]=l_time
        d_transfer[2]=l_userid
        return d_transfer
