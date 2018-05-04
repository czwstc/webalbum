class PhotoPO:
    def __init__(self):
        self.photo_id = None
        self.photo_name = None
        self.album_id=None
        self.update_date= None
        self.photo_description=None
        self.file_name=None
        self.is_public=None
        self.user_id=None


    def get_photo_name(self):
        return self.photo_name

    def get_album_id(self):
        return self.album_id
    def get_user_id(self):
        return self.user_id

    def get_file_name(self):
        return self.file_name
    def get_photo_id(self):
        return self.photo_id
    def get_photo_description(self):
        return self.photo_description
    def get_is_public(self):
        return self.is_public
    def get_update_date(self):
        return self.update_date

    def set_photo_id(self, photo_id):
        self.photo_id = photo_id

    def set_update_date(self,update_date):
        self.update_date=update_date

    def set_is_public(self,is_public):
        self.is_public=is_public
    def set_file_name(self,file_name):
        self.file_name=file_name
    def set_photo_description(self,photo_description):
        self.photo_description=photo_description
    def set_photo_name(self,photo_name):
        self.photo_name=photo_name
    def set_album_id(self,album_id):
        self.album_id=album_id
    def set_user_id(self,user_id):
        self.user_id=user_id

    '''def toString(self):
        return str(self.photo_id)+' ' + self.dianzan_name+ ' ' + self.time'''