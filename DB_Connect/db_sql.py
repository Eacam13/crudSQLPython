import pymysql.cursors

class DB_Connect:
    def __init__(self):
        try:
            self.conecta_db = pymysql.connect(user='root',
                                              password='',
                                              host='localhost',
                                              database='projetocrud')
            self.cursor = self.conecta_db.cursor()

        except Exception as error:
            print(error)



