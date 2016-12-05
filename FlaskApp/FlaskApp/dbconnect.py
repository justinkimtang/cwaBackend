import MySQLdb

def connection():
    conn = MySQLdb.connect(user = "root",
                           passwd = "2511",
                           db = "flasktest")
    c = conn.cursor()
    return c, conn
