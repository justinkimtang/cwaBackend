import MySQLdb
import getpass

delete = getpass.getpass("Are you sure you want to delete the database y/n")

if(delete == 'y'):
    password = getpass.getpass("Input mysql password:")
    cnx = MySQLdb.connect(user='root', passwd = password)
    cursor = cnx.cursor()
    try:
            cursor.execute("DROP DATABASE cwatest")
    except MySQLdb.Error as err:
            print(err)
    else:
            print("DATABASE DROPPED")
else:
        print("Bye :'(")
        exit(0)
