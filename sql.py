import sqlite3

conn = sqlite3.connect("blog.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS posts(posts TEXT, title TEXT)""" )

c.execute("""INSERT INTO posts VALUES ('hello', 'Hello world')""")
c.execute("""INSERT INTO posts VALUES ('blog1', 'This is Blog 1')""")
c.execute("""INSERT INTO posts VALUES ('blog2', 'This is Blog2')""")
c.execute("""INSERT INTO posts VALUES ('hello', 'This is Blog3')""")
c.execute("""INSERT INTO posts VALUES ('hello', 'This is Blog4')""")

conn.commit()
conn.close()