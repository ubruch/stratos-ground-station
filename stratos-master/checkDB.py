
import time, os,sys, sqlite3, datetime


location = "C:\\sqlite\db\pythonsqlite.db"


######################################33
#VIEWING THE DATABASE
connection = sqlite3.connect(location)
cursor = connection.cursor()
query = "SELECT * FROM parametersTable;"
cursor.execute(query)
results = cursor.fetchall()
print(results)


for i in range(0,5):
    print("")


query = "SELECT * FROM historicalsTable;"
cursor.execute(query)
results = cursor.fetchall()
print(results)


for i in range(0,5):
    print("")


query = "SELECT * FROM logsTable;"
cursor.execute(query)
results = cursor.fetchall()
print(results)


for i in range(0,5):
    print("")


query = "SELECT * FROM missionsTable;"
cursor.execute(query)
results = cursor.fetchall()
print(results)


cursor.close()
connection.close()
