# importing the sqlite3 module
import sqlite3
#files list
fileList = ('information.docx','Hello.txt','my/image.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#connect to database
conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()

# creating the database table if the table does not already exists
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fileName TEXT \
                )")

#for loop to add only files that endswith '.txt'
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES(?)",(file,))
            print(file)                        
    conn.commit()
#close the Database connection
conn.close()

