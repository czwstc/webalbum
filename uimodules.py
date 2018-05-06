import tornado.web

class Navbar(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "common/module-navbar.html")

class Dialog(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "common/module-dialog.html")