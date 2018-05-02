class FeedPO:
    def __init__(self):
        self.id = None
        self.photo_id = None
        self.user_id = None
        self.reason = None
        self.time = None

    def get_reason(self):
        return self.reason

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time

    def get_photo_id(self):
        return self.photo_id

    def get_user_id(self):
        return self.user_id

    def set_photo_id(self, photo_id):
        self.photo_id = photo_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_time(self, time):
        self.time = time

    def set_reason(self, reason):
        self.reason = reason
