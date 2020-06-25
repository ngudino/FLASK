import pymysql


class DataBase():
    #__host = "10.1.1.32"
    __host = "localhost"
    __user = ""
    __passw = ""
    __dbname = ""
    __cnn = ""
    __cursor = ""

    def __init__(self, phost="localhost", puser="root", ppassw="", dbname="intranet"):
        self.__host = phost
        self.__user = puser
        self.__pass = ppassw
        self.__dbname = dbname

    def conectarDB(self):
        self.__cnn = pymysql.connect(self.__host, self.__user, self.__pass, self.__dbname)
        # print(self.__cnn)

    def leerDatos(self, sql, valores=""):
        cursor = self.__cnn.cursor(pymysql.cursors.DictCursor)
        if valores != "":
            cursor.execute(sql, (valores,))
        else:
            cursor.execute(sql)
        self.__cursor = cursor
        cursor.close()
        #return cursor.fetchall()
        return self.__cursor.fetchall()

    def getCursor(self):
        return self.__cursor

    def inmodDatos(self, sql, valores):
        cursor = self.__cnn.cursor(pymysql.cursors.DictCursor)
        #try:
        cursor.execute(sql, valores)
        self.__cnn.commit()
        self.__cursor = cursor
        cursor.close()
        #except:
        #    self.__cnn.rollback()        

    def cerrarCnn(self):
        self.__cnn.close()
