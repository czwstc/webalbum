import pymysql

class DataBaseManager:
    def __init__(self):
        self.conn = None

    def DataBaseManager(self, Host, Port, User, Passwd, DB, Charset):
        try:
            self.conn = pymysql.Connect(
                host=Host,
                port=Port,
                user=User,
                passwd=Passwd,
                db=DB,
                charset=Charset
            )
        except:
            print("open error")


    def closeConection(self):
        try:
            self.conn.commit()
            self.conn.close()
        except:
            print("end error")
