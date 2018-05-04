class albumPO:
    def __init__(self):
        #self.id = None
        self.album_id=None
        self.album_name=None
        self.album_description=None
        self.cover_id=None
        self.user_id=None
        self.create_date=None
        self.edit_date=None

    #def get_id(self):
        #return self.id

    def get_album_id(self):
        return self.album_id

    def get_album_name(self):
        return self.album_name

    def get_album_description(self):
        return self.album_description

    def get_cover_id(self):
        return self.cover_id

    def get_user_id(self):
        return self.user_id

    def get_create_date(self):
        return self.create_date

    def get_edit_date(self):
        return self.edit_date

    def set_album_id(self, album_id):
        self.album_id = album_id

    def set_album_name(self, album_name):
        self.album_name = album_name

    def set_album_description(self, album_description):
        self.album_description = album_description

    def set_cover_id(self, cover_id):
        self.cover_id = cover_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_create_date(self, create_date):
        self.create_date = create_date

    def set_edit_date(self, edit_date):
        self.edit_date = edit_date


    def toString(self):
        return str(self.album_id) +' '+self.album_name+' ' + self.album_description+' '+ self.cover_id+' ' + self.user_id+' ' + self.create_date+' ' + self.edit_date