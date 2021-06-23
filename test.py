
import sqlite3

sqliteConnection = sqlite3.connect('db.sqlite3')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
tagname = "test"
client_id = 1
avg_pol = 1
query = "insert into app1_client_tag (tagname, client_id,polarity ) Values('{}',{},{})".format(tagname, client_id, avg_pol)
cursor.execute(query)
sqliteConnection.commit()
sqliteConnection.close()
