# sql
# СУБД - система управления базами данных
# реляционные и нереляционные
# CRUD create reed update delete

import sqlite3

db = sqlite3.connect('29_3.db')

c = db.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS
user(
name text,
hobby text,
view integer,
nick text
) ''')

# create
# c.execute("INSERT INTO user VALUES ('akeb','qwert',5,'ogil')")
# c.execute("INSERT INTO user VALUES ('ake','qw1234',10,'gil')")
# c.execute("INSERT INTO user VALUES ('aki','qwerts',1,'ogPl')")
c.execute("INSERT INTO user VALUES ('aka','qwer22',4,'ogol')")
# delete
# c.execute("DELETE FROM user WHERE view <=1 ")
# c.execute("DELETE FROM user WHERE hobby == 5")



c.execute("UPDATE user SET name='гига' WHERE rowid==1 ")



# reed




c.execute("SELECT rowid,* FROM user")

item = c.fetchall()
for i in item:
    print(i)

# print(c.fetchall())
# print(c.fetchmany(3))
# print(c.fetchone())





db.commit()
db.close()
