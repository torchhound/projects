import sqlite3

sqliteFile = "practice.sqlite"
table1 = "users"
field1 = "type"
fieldType = "INTEGER"

conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS {}".format(table1))
c.execute("CREATE TABLE {table1} ({field1} {fieldType})"\
        .format(table1=table1, field1=field1, fieldType=fieldType))

#c.execute("CREATE TABLE {t1} ({f1} {ft1} PRIMARY KEY)"\
#        .format(t1=table1, f1=field1, ft1=fieldType))

conn.commit()
conn.close()
