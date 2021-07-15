class mysql:
    def __init__(self,host,port,user,passwd,db):
        import pymysql
        mydb=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset='utf8')
        cursor = mydb.cursor()
        self.cursor=cursor
    def excute(self,value):
        self.cursor.execute(value)
    def fetchone(self):
        self.cursor.fetchone()
    def fetchall(self):
        self.cursor.fetchall()
    def dbclose(self):
        self.cursor.close()
