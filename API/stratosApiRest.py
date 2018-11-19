import sqlite3
from flask import Flask, render_template, request, jsonify




######################################################
################ GLOBAL VARIABLES ####################
######################################################
DATABASE = "C:/Users/Pen/Desktop/Programmierung/Stratos/datenbank.db"
PARAMS_TABLE = "parametersTable"
HISTORICAL_TABLE = "historicalsTable"
LOGS_TABLE = "logsTable"
app = Flask(__name__)



#main web site
@app.route('/')
def startPage():
    return(render_template('home.html'))


#docs web site
@app.route('/docs')
def docsPage():
    return(render_template('docs.html'))


#about web site
@app.route('/about')
def aboutPage():
    return(render_template('about.html'))


#contact web site
@app.route('/contact')
def contactPage():
    return(render_template('contact.html'))

#lastData web site
@app.route('/lastData')
def getLastData():

    id = request.args.get('id')
    
    #if no id is specified, use id 1
    if(id==None):
        id="1"
        
    #if wrong id is requested, return wrongId site
    exists = idExists(id)
    if( exists == False ):
        return(render_template('wrongId.html'))
        
        
    if(id==1 or id=='1'):
        id=""

    #get Data and parameter names
    lastValues, names = downloadLastData(id)

    #process the data mode queried
    mode = request.args.get('mode')

	#method that returns a json to download
    if(mode=="json"):
        return(jsonify({'lastData': lastValues}))
	#method that displays a table with the last data in the navigator
    else:
        templateData = {"lastValues":lastValues, "names":names}
        return(render_template('lastData.html', **templateData))


#method selects the last data from the database and also gets the names
def downloadLastData(id):

	connection = sqlite3.connect(DATABASE)
	cursor = connection.cursor()

	query = "SELECT * FROM " + PARAMS_TABLE + id
	cursor.execute(query)
	results = cursor.fetchall()
   #get the column names
	names = [description[0] for description in cursor.description]

	lastData = []

	for j in range(0, len(results)):
		lastValuesDictionary = {}
		for i in range(0,len(names)):
			lastValuesDictionary[str(names[i])] = str(results[j][i])
		lastData.append(lastValuesDictionary)

	print(lastData)

	cursor.close()
	connection.close()
	return lastData, names


#historicalData site
@app.route('/historicalData')
def getHistoricalData():

    id = request.args.get('id')
    
    #if no id is specified, use id 1
    if(id==None):
        id="1"
        
    #if wrong id is requested, return wrongId site    
    exists = idExists(id)
    if( exists == False ):
        return(render_template('wrongId.html'))
        
        
    if(id==1 or id=='1'):
        id=""

    #get Data and parameter names
    historicalValues, names = downloadHistoricalData(id)

    #process the data mode queried
    mode = request.args.get('mode')

	#method that returns a json to download
    if(mode=="json"):
        return(jsonify({'historicalData': historicalValues}))
	#method that displays a table with the last data in the navigator
    else:
        templateData = {"historicalValues":historicalValues, "names":names}
        return(render_template('historicalData.html', **templateData))


#method selects the last data from the database and also gets the names
def downloadHistoricalData(id):

	connection = sqlite3.connect(DATABASE)
	cursor = connection.cursor()

	query = "SELECT * FROM " + HISTORICAL_TABLE + id
	cursor.execute(query)
	results = cursor.fetchall()
   #get the column names
	names = [description[0] for description in cursor.description]

	historicalData = []

	for j in range(0, len(results)):
		lastValuesDictionary = {}
		for i in range(0,len(names)):
			lastValuesDictionary[str(names[i])] = str(results[j][i])
		historicalData.append(lastValuesDictionary)

	print(historicalData)

	cursor.close()
	connection.close()
	return historicalData, names


#logsData site
@app.route('/logsData')
def getLogsData():
    #get Data and parameter names
    logsValues, names = downloadLogsData()

    #process the data mode queried
    mode = request.args.get('mode')

	#method that returns a json to download
    if(mode=="json"):
        return(jsonify({'logsData': logsValues}))
	#method that displays a table with the last data in the navigator
    else:
        templateData = {"logsValues":logsValues, "names":names}
        return(render_template('logsData.html', **templateData))


#method selects the last data from the database and also gets the names
def downloadLogsData():

	connection = sqlite3.connect(DATABASE)
	cursor = connection.cursor()

	query = "SELECT * FROM " + LOGS_TABLE
	cursor.execute(query)
	results = cursor.fetchall()
   #get the column names
	names = [description[0] for description in cursor.description]

	logsData = []

	for j in range(0, len(results)):
		lastValuesDictionary = {}
		for i in range(0,len(names)):
			lastValuesDictionary[str(names[i])] = str(results[j][i])
		logsData.append(lastValuesDictionary)

	print(logsData)

	cursor.close()
	connection.close()
	return logsData, names




#method that checks if an ID exists
def idExists(id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    query = "SELECT mission FROM missionsTable"
    cursor.execute(query)
    results = cursor.fetchall()
    print(results[0])
    cursor.close()
    connection.close()

    for i in range(len(results)):
        print(int(id))
        print(results[i])
        print(int(id) not in (results[i]))
        if( int(id) in results[i] ):
            return True
    return False




#main method
if __name__ == '__main__':

	app.run(debug = True, host = '0.0.0.0')
