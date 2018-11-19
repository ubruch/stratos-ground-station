import sqlite3, datetime


location = "C:/Users/Pen/Desktop/Programmierung/Stratos/datenbank.db"

conn = sqlite3.connect(location)
c = conn.cursor()

now = datetime.datetime.now()
timeStamp = now.strftime("%Y-%m-%d %H:%M:%S")



#reseting SQL tables
c.execute("DROP TABLE IF EXISTS parametersTable")
c.execute("DROP TABLE IF EXISTS historicalsTable")
c.execute("DROP TABLE IF EXISTS parametersTable2")
c.execute("DROP TABLE IF EXISTS historicalsTable2")
c.execute("DROP TABLE IF EXISTS logsTable")
c.execute("DROP TABLE IF EXISTS missionsTable")




#create parameters or historicalsTable if they do not already exist
c.execute("CREATE TABLE IF NOT EXISTS parametersTable (id INTEGER PRIMARY KEY, name VARCHAR, value VARCHAR, code INTEGER, lastActualization DATETIME," \
                                                "description VARCHAR, units VARCHAR, lastValue VARCHAR, dateType VARCHAR, status VARCHAR, "\
                                                "maxValue VARCHAR, minValue VARCHAR);")
c.execute("CREATE TABLE IF NOT EXISTS historicalsTable (id INTEGER PRIMARY KEY, value VARCHAR, code INTEGER, insertTime DATETIME);")
c.execute("CREATE TABLE IF NOT EXISTS logsTable (id INTEGER PRIMARY KEY, data VARCHAR, insertTime DATETIME);")
c.execute("CREATE TABLE IF NOT EXISTS missionsTable (id INTEGER PRIMARY KEY, mission INTEGER, description VARCHAR, paramsTable VARCHAR, historicalTable VARCHAR, insertTime DATETIME);")


#inserting into missionsTable
c.execute("INSERT INTO missionsTable (mission, description, paramsTable, historicalTable, insertTime) VALUES (1, \'Stratos Mission 1\', \'parametersTable\', \'historicalsTable\', \'" + timeStamp + "\')")


#inserting the actual values
c.execute("INSERT INTO parametersTable (code, value, name, lastActualization, description, units, lastValue, dateType, status, maxValue, minValue)" \
                                        "VALUES (100, \'25\' ,\'temperature\',\'" + timeStamp + "\', \'Temperature of the balloon\', \'ºC\'," \
                                        "20, \'float\',  \'OK\', 50, -50);")

c.execute("INSERT INTO parametersTable (code, value, name, lastActualization, description, units, lastValue, dateType, status, maxValue, minValue)" \
                                        "VALUES (20, \'2500\' ,\'heigth\',\'" + timeStamp + "\', \'Height of the balloon\', \'m\'," \
                                        "125, \'float\',  \'OK\', 40000, -20);")

c.execute("INSERT INTO parametersTable (code, value, name, lastActualization, description, units, lastValue, dateType, status, maxValue, minValue)" \
                                        "VALUES (1, \'1\' ,\'mission\',\'" + timeStamp + "\', \'Number of STRATOS mission \', \'none\'," \
                                        "1, \'integer\',  \'OK\', 5, 0);")


#inserting empty values in the historical table
c.execute("INSERT INTO historicalsTable (code, value, insertTime) VALUES (100,\'20\', \'" + timeStamp + "\');")

c.execute("INSERT INTO historicalsTable (code, value, insertTime) VALUES (20,\'125\', \'" + timeStamp + "\');")

c.execute("INSERT INTO historicalsTable (code, value, insertTime) VALUES (200,\'1\', \'" + timeStamp + "\');")


conn.commit()
c.close()
conn.close()