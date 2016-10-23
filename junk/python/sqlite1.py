import sqlite3

sqliteFile = "practice1.sqlite"

conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Kingdom")
c.execute("CREATE TABLE Kingdom(Id INT, Name TEXT)")
c.execute("INSERT INTO Kingdom VALUES(1, 'Britain')")

conn.commit()

try:
    c.execute("SELECT * FROM Kingdom")
    rows = c.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(e)

conn.close()
