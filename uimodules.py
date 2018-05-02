import tornado.web
class Navbar(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "common/module-navbar.html")

class Bottom(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "common/module-bottom.html")

class Dialog(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "common/module-dialog.html")