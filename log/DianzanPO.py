class DianzanPO:
    def __init__(self):
        self.id = None
        #self.photo_id = None
        self.user_id = None
        #self.time = None
        self.feed_id = None

    def get_feed_id(self):
        return self.feed_id

    def get_id(self):
        return self.id

    #def get_time(self):
       # return self.time

    #def get_photo_id(self):
        #return self.photo_id

    def get_user_id(self):
        return self.user_id

    #def set_photo_id(self, photo_id):
        #self.photo_id = photo_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    #def set_time(self, time):
        #self.time = time

    def set_feed_id(self, feed_id):
        self.feed_id = feed_id

    def toString(self):
        return str(self.photo_id)+' ' + self.user_id+ ' '