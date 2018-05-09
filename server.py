#coding=UTF-8
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
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.locale
import unicodedata
import uimodules


from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="47.104.68.55:3306", help="blog database host")
define("mysql_database", default="test", help="blog database name")
define("mysql_user", default="root", help="blog database user")
define("mysql_password", default="linux", help="blog database password")

# A thread pool to be used for password hashing with bcrypt.
executor = concurrent.futures.ThreadPoolExecutor(2)





class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r"/", HomeHandler),
            #注册，登录，登出，账号删除，个人资料展示页面，个人资料编辑-丰玉霖
            url(r"/signup", AuthCreateHandler),
            url(r"/login", AuthLoginHandler),
            url(r"/logout", AuthLogoutHandler),
            url(r"/close", UserDeleteHandler),
            url(r"/pro", ProfileHandler),
            url(r"/u/([0-9]+)/profile/*", ProfileHandler),
            url(r"/proedit", ProfileEditHandler),

            #新建相册，相册列表,相册编辑，相册删除-阙中元，魏晓飞
            url(r"/u/([0-9]+)/photos/*", Photosall),
            url(r"/albums/new", AlbumCreateHandler, name="AlbumCreate"),
            url(r"/albums/*", MyAlbumsHandler,name="MyAlbums"),
            url(r"/u/([0-9]+)/albums/*", AlbumsListHandler),
            url(r"/albums/edit", AlbumEditHandler),
            url(r"/albums/delete", AlbumDeleteHandler),

            #上传相片，相片列表，单个相片显示页面，相片删除，朋友圈-唐永剑，贾超，姚彬，徐怡阳，张光伟，李佳袁
            url(r"/photos/new", PhotosUploadHandler, name="PhotosUpload"),
            url(r"/u/([0-9]+)/albums/([0-9]+)", PhotosListHandler),             #<-这是相片列表
            url(r"/u/([0-9]+)/albums/([0-9]+)/play", PhotoPlayHandler),         #<-这是幻灯播放
            url(r"/u/([0-9]+)/albums/([0-9]+)/([0-9]+)", PhotoHandler),        #<-这是单张照片浏览        
            url(r"/u/([0-9]+)/albums/([0-9]+)/([0-9]+)/delete", PhotoDeleteHandler),
            url(r"/feed/*", FeedHandler, name="feed"),
            url(r"/test/*", jc_PhotoPlayHandler)

        ]
        settings = dict(
            website_title=u"NEU相册",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"Navbar":uimodules.Navbar,
                        "Dialog":uimodules.Dialog},
            xsrf_cookies=False,
            cookie_secret="1234567892015neuee",
            login_url="/login",
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)
        tornado.locale.set_default_locale("zh_CN")
        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

        self.maybe_create_tables()

    def maybe_create_tables(self):
        try:
            self.db.get("SELECT COUNT(*) from users;")
        except MySQLdb.ProgrammingError:
            subprocess.check_call(['mysql',
                                   '--host=' + options.mysql_host,
                                   '--database=' + options.mysql_database,
                                   '--user=' + options.mysql_user,
                                   '--password=' + options.mysql_password],
                                  stdin=open('schema.sql'))


from basehandler import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        self.render("home.html",user=self.current_user)


from handler.feedhandler import FeedHandler
from handler.userhandler import *
from handler.albumhandler import *
from handler.photohandler import *

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
