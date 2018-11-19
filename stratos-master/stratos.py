import time, os, sys, sqlite3
from datetime import datetime



######################################################
################ GLOBAL VARIABLES ####################
######################################################
DATABASE = "C:\\sqlite\db\pythonsqlite.db"
PARAMS_TABLE = "parametersTable"
HISTORICAL_TABLE = "historicalsTable"
LOGS_TABLE = "logsTable"



######################################################
########## CLASS THAT GETS THE DATA FILE #############
######################################################
class GetNewFile:

    def __init__(self):

        self.file = None
        self.path = None
        self.possibleFiles = []
        self.dates = []

        self. getFiles()
        self.getLatestFile()


    #method that gets the .txt files in the folder
    def getFiles(self):

        self.path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])

        for (path, directories, files) in os.walk( self.path ):
            for fileName in files:
                if ".txt" in fileName:
                    self.possibleFiles.append(fileName)


    #method that finds the latest data file
    def getLatestFile(self):

        for fileName in self.possibleFiles:
            try:
                self.dates.append( datetime( int(fileName[0:4]), int(fileName[4:6]), int(fileName[6:8]), int(fileName[8:10]), int(fileName[10:12]), int(fileName[12:14]) ) )
            except:
                pass

        newest = max(self.dates)
        index = self.dates.index(newest)

        self.file = self.possibleFiles[index]



######################################################
########## CLASS THAT PROCESSES THE DATA #############
######################################################
class ProcessFile:

    def __init__(self, fileName):

        self.fileName = fileName
        self.codeNames = []
        self.data = {}
        self.queryParameters = []

        now = datetime.now()
        self.timeStamp = now.strftime("%Y-%m-%d %H:%M:%S")

        self.readData()
        self.processParameters()


    #method that reads the data and stores it into a dictionary
    def readData(self):

        print("opening file: " + str(self.fileName))
        f = open(self.fileName,'r')
        line = f.readlines()[-1]
        f.close()

        #os.system("scp FILE USER@SERVER:PATH")

        #we update the logs table with the new received data
        self.updateLogs(line)

        data = line.split(";")

        for parameter in data[1:]:

            splittedParameter = parameter.split(":")
            self.data[ splittedParameter[0] ] = splittedParameter[1]

        print("data gathered:  " + str(self.data))


    #method that processes the parameter by checking if the value is correct and updating the databases
    def processParameters(self):

        #we check if the misson ID already has a table, or if it is a new one
        error = self.checkMissionID()
        if(error == True):
            print("No mission ID was found in the data, an error was triggered")
            sys.exit()

        #we iterate through the parameters in order to process them
        for parameter in self.data:

            isParamGood = True

            #first we check if the parameter exists
            parameterExists = self.doesParameterExist(parameter)


            #if the parameter does not exist, we add it as an unknown parameter
            if(parameterExists=="no"):
                self.addNewParameter(parameter, self.data[parameter])
                continue

            #otherwise, we move the old value to the historical table
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            query = "SELECT value, lastActualization FROM " + PARAMS_TABLE + " WHERE code = " + parameter + ";"
            cursor.execute(query)
            results = cursor.fetchall()
            oldValue = results[0][0]
            cursor.execute("INSERT INTO " + HISTORICAL_TABLE + " (code, value, insertTime) VALUES (" + parameter + ",\'" + results[0][0] +"\', \'" + results[0][1] + "\');")
            connection.commit()


            #updating the current values of the sensor
            cursor.execute("UPDATE " + PARAMS_TABLE + "  SET value = \'" + self.data[parameter] + "\' WHERE code = " + parameter + ";")
            cursor.execute("UPDATE " + PARAMS_TABLE + "  SET lastActualization = \'" + self.timeStamp + "\' WHERE code = " + parameter + ";")
            cursor.execute("UPDATE " + PARAMS_TABLE + "  SET lastValue = \'" + oldValue + "\' WHERE code = " + parameter + ";")
            connection.commit()


            #we call the corresponding handler to check if the new value is correct
            query = "SELECT dateType FROM " + PARAMS_TABLE + " WHERE code = " + parameter + ";"
            cursor.execute(query)
            results = cursor.fetchall()
            if(results[0][0]=="integer"):
                isParamGood = Handlers.integerHandler(parameter, self.data[parameter])
            elif(results[0][0]=="float"):
                isParamGood = Handlers.floatHandler(parameter, self.data[parameter])
            elif(results[0][0]=="string"):
                isParamGood = True
                #isParamGood = Handlers.stringHandler(self.data[parameter])
            else:
                print("upsi")

            #if there is an error in the parameter (either dataType or in the value) we update the status of the sensor to ERROR
            if(isParamGood == False):
                print("error with data type ( " + results[0][0] + " ) in parameter: " + parameter + "   " + self.data[parameter])
                cursor.execute("UPDATE " + PARAMS_TABLE + "  SET status = \'ERROR\' WHERE code = " + parameter +";")
                connection.commit()
            else:
                cursor.execute("UPDATE " + PARAMS_TABLE + "  SET status = \'OK\' WHERE code = " + parameter +";")
                connection.commit()

                cursor.close()
                connection.close()


    #method that checks wether a parameter exists in the parameters table
    def doesParameterExist(self, code):

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        query = "SELECT * FROM " + PARAMS_TABLE + " WHERE code = " + code + ";"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        if( len(results)==0 ):
            return "no"
        else:
            return results[0]


    #method that adds a new unknown parameter
    def addNewParameter(self, code, value):

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        #making the new name and obtaining the timestamp
        newParamName = "unknown_" + code

        #inserting the new unknown parameter in the current and historical tables
        c.execute("INSERT INTO " + PARAMS_TABLE + "  (code, value, name, lastActualization, description, units, lastValue, dateType, status, maxValue, minValue)" \
                                                "VALUES (" + code + ",\'" + value + "\',\'"+ newParamName +"\', \'" + self.timeStamp + "\' , \'unknown parameter\'," \
                                                 "\'\', \'value\', \'string\',  \'OK\', \'\', \'\');")
        c.execute("INSERT INTO " + HISTORICAL_TABLE + "  (code, value, insertTime) VALUES (" + code + ",\'" + value + "\', \'" + self.timeStamp + "\');")

        conn.commit()
        c.close()
        conn.close()


    #method that updates the logs table
    def updateLogs(self, data):

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        query = "INSERT INTO " + LOGS_TABLE + "(data, insertTime) VALUES(\'" + data + "\', \'" + self.timeStamp + "\');"
        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()


    #method that checks if the actual mission is new or not
    def checkMissionID(self):

        error = True

        #first we check if we have received the mission ID
        for parameter in self.data:
            if( parameter == '1'):
                error = False

        #if we havent found an ID, we return error
        if(error == True):
            return True

        #we check if the received id exists
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        query = "SELECT mission FROM missionsTable"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        aux = False
        for i in range(len(results)):
            if( int(self.data['1']) in results[0] ):
                aux = True

        if( aux == False):
            print("new mission ID, creating new Table and updating Missions Table")
            self.newMission()
        return False


    #method that updates the missionsTable and creates new paramsTable and historicalsTable
    def newMission(self):

        global PARAMS_TABLE, HISTORICAL_TABLE

        id = int(self.data['1'])
        paramsTable = "parametersTable" + str(id)
        historicalTable = "historicalsTable" + str(id)
        description = "Stratos Mission " + str(id)
        PARAMS_TABLE = paramsTable
        HISTORICAL_TABLE = historicalTable

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO missionsTable (mission, description, paramsTable, historicalTable, insertTime) VALUES " \
            "("+ str(id) +", \'" + description + "\', \'" + paramsTable + "\', \'" + historicalTable + "\', \'" + self.timeStamp + "\')")
        cursor.execute("CREATE TABLE IF NOT EXISTS " + paramsTable + " (id INTEGER PRIMARY KEY, name VARCHAR, value VARCHAR, code INTEGER, lastActualization DATETIME," \
                                                        "description VARCHAR, units VARCHAR, lastValue VARCHAR, dateType VARCHAR, status VARCHAR, "\
                                                        "maxValue VARCHAR, minValue VARCHAR);")
        cursor.execute("CREATE TABLE IF NOT EXISTS " + historicalTable + " (id INTEGER PRIMARY KEY, value VARCHAR, code INTEGER, insertTime DATETIME);")
        connection.commit()
        cursor.close()
        connection.close()

        print("alles in ordnung")


#class that hosts the handlers for the received values
class Handlers:

    #integer handler
    def integerHandler(code, value):

        #check if the value is integer
        try:
            value = int(value)
        except:
            return False

        max = Handlers.getMax(code)
        min = Handlers.getMin(code)

        #check that value is within range
        if( value > max or value < min  ):
            return False

        return True


    #float handler
    def floatHandler(code, value):

        #check if the value is float
        try:
            value = float(value)
        except:
            return False

        max = Handlers.getMax(code)
        min = Handlers.getMin(code)

        #check that value is within range
        if( value > max or value < min  ):
            return False

        return True


    #string handler
    def stringHandler(value):

        #check if the value is float
        if( isinstance(value, str) == False ):
            return False

        return True


    #max getter
    def getMax(code):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        query = "SELECT maxValue FROM " + PARAMS_TABLE + " WHERE code = " + code + ";"
        cursor.execute(query)
        results = cursor.fetchall()
        max = float(results[0][0])
        return max


    #min getter
    def getMin(code):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        query = "SELECT minValue FROM " + PARAMS_TABLE + " WHERE code = " + code + ";"
        cursor.execute(query)
        results = cursor.fetchall()
        min = float(results[0][0])
        return min



######################################################
#################  MAIN PROGRAM ######################
######################################################
if __name__ == "__main__":

    os.system("cls")
    fileGetter = GetNewFile()
    processObject = ProcessFile( fileGetter.file )




##
