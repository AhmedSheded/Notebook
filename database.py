import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='NoteBook'
)

mycursor = db.cursor()
# mycursor.execute('CREATE DATABASE NoteBook')
#
# mycursor.execute("CREATE TABLE Notes(id int PRIMARY KEY AUTO_INCREMENT,"
#                  "title VARCHAR(100) NOT NULL,"
#                  "subject TEXT NOT NULL,"
#                  "created_date datetime NOT NULL)")
# db.commit

# mycursor.execute('drop table Notes')

# mycursor.execute("INSERT Notes(title, subject, created_date) "
#                  "VALUES(%s, %s, %s)",
#                  ("head", "body", datetime.now()))
# db.commit()



