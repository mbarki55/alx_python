import MySQLdb as Server
from sys import argv

config_connect = Server.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], database=argv[3])

cursor = config_connect.cursor()

cursor.execute('''SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.state_id ASC, cities.id ASC;
                ''')

rows = cursor.fetchall()

for row in rows:
  print(row)

cursor.close()
config_connect.close()