import sqlite3

#Location of DB, dont forget to change!
location = "C:/Users/Pen/Desktop/Programmierung/Stratos/datenbank.db"

#Function to create some Distance between the Results
def distance(emptyRows):
    for i in range(0,emptyRows):
        print("")
    
#VIEWING THE DATABASE
connection = sqlite3.connect(location)
cursor = connection.cursor()
query = "SELECT * FROM parametersTable;"
cursor.execute(query)
results = cursor.fetchall()
print("Parameter Tables:")
print("ID, Name, Value, Code, Last Actualization, Description, Unit, Last Value, Datatype, Status, Max. Value, Min. Value")
for line in results:
    print(line)

distance(2)

query = "SELECT * FROM historicalsTable;"
cursor.execute(query)
results = cursor.fetchall()
print("Hisorical Tables:")
print("ID, Value, Code, Insert Time")
for line in results:
    print(line)

distance(2)

query = "SELECT * FROM logsTable;"
cursor.execute(query)
results = cursor.fetchall()
print("Log Tables:")
print("ID, data, Insert Time")
for line in results:
    print(line)

distance(2)

query = "SELECT * FROM missionsTable;"
cursor.execute(query)
results = cursor.fetchall()
print("Mission Tables:")
print("ID, Mission, Description, Parameter Table, Historical Table, Insert Time")
for line in results:
    print(line)


cursor.close()
connection.close()