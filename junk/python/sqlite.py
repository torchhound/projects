import sqlite3

sqliteFile = "practice.sqlite"
table1 = "users"
field1 = "type"
fieldType = "INTEGER"
fieldType1 = "STRING"

conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

c.execute("CREATE_TABLE {table1} ({field1} {fieldType})"\
        .format(table1=table1, field1=field1, fieldType=fieldType))

c.execute("CREATE_TABLE {t1} ({f1} {ft1} PRIMARY KEY)"\
        .format(t1=table1, f1=field1, ft1=fieldType1))

conn.commit()
conn.close()
