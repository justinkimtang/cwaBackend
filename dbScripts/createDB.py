import MySQLdb
import getpass
from  import tableSQL TABLES, TABLES2

def create_database():
        password = getpass.getpass("Input mysql password:")
        try:
                DB_NAME ="cwatest"
                cnx = MySQLdb.connect(user='root', passwd= password)
                cursor = cnx.cursor()
        except MySQLdb.Error as err:
                print("Failed to connect to db{}".format(err))
                exit(1)
        try:
                cursor.execute("CREATE SCHEMA IF NOT EXISTS cwatest")
                cursor.execute("USE cwatest")
        except MySQLdb.Error as err:
                print("Failed to create database: {}".format(err))
                exit(1)
        try:
                cnx = MySQLdb.connect(user='root',passwd=password,db = DB_NAME)
                cursor = cnx.cursor()
        except MySQLdb.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                        create_database(cursor)
                        cnx.database = DB_NAME
                else:
                        print(err)
                        exit(1)
        for name, ddl in TABLES.iteritems():
                try:
                        print("CREATE {}".format(name))
                        cursor.execute(ddl)
                except MySQLdb.Error as err:
                        print(err)
                else:
                        print("OK")

        for name, ddl in TABLES2.iteritems():
                try:
                        print("CREATE {}".format(name))
                        cursor.execute(ddl)
                except MySQLdb.Error as err:
                        print(err)
                else:
                        print("OK")


create_database()
