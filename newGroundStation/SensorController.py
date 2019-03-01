#created by jwenner
#edited by jwenner
import traceback

import requests
from flask import Flask, json, logging


#Class to recieve sensor data and fill them in SensorView
class SensorController:

    app = Flask(__name__)  # Declaring aplication

    # Ending of the url
    # port is 8050
    @app.route('/localEndPoint', methods=['POST'])
    def RESTservice1(self):
        #TODO
        return 200

    def RESTservice2(self):
        #TODO
        return 200

    def RESTservice3(self):
        #TODO
        return 200

    def RESTrequest(self):
        url = 'http://url:port/direction'
        data = None
        try:
            headers = {
                'Content-Type': 'application/json',
                'X-CAMERA': 'fixed'
            }
            payload = {
            }

            response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
            data = response.json()
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))

        return 'Request done. Answer get : ' + str(data)


    if __name__ == '__main__':
        app.run(debug=True, port=8050)
