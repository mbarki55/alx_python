

import MySQLdb as Server
from sys import argv

config_connect = Server.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])

cursor = config_connect.cursor()

cursor.execute("SELECT * FROM states WHERE name ='{}' ORDER BY id ASC".format(argv(4)))

rows = cursor.fetchall()

for row in rows:
    if row[1][0]=='N':
     print(row)

cursor.close()
config_connect.close()

