import MySQLdb as Server
from sys import argv

config_connect = Server.connect(host='localhost', port=3306, user=argv[1], password=argv[2], db=argv[3])

cursor = config_connect.cursor()

query = '''SELECT cities.name FROM cities
          JOIN states ON cities.state_id = states.id
          WHERE state_id = (SELECT id FROM states WHERE name = %s)
          ORDER BY cities.id ASC'''


cursor.execute(query, (argv[4],))

rows = cursor.fetchall()

result = ', '.join(row[0] for row in rows)
print(result)


cursor.close()
config_connect.close()