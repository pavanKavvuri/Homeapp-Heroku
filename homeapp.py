from flask import Flask, jsonify,request, session, abort, flash, redirect
from flask import render_template
import time as t
app = Flask(__name__)
import os
import json
import datetime
from flask import jsonify


app = Flask(__name__)

@app.route('/getData/temp/<temp>/hum/<hum>', methods=['GET'])
def dataGet(temp, hum):
    try:
        with open('homeapp.json', 'r') as dataFile:
            tmp = json.load(dataFile)
            dataFile.close()
        tmp['Temperature'] = temp
        tmp['Humidity'] = hum
    except Exception as e1:
        print (str(e1))
    

    try:
        with open('homeapp.json', 'w') as dataFile:
            json.dump(tmp, dataFile)
    except  Exception as e4:
        print(str(e4)) 

    return jsonify(tmp)

    

@app.route('/slides', methods=['POST'])
def switch():

    try:
        _state = request.form['state']
        _ID = request.form['ID']
        print(_state)
        print(_ID)
    except Exception as e:
        print(str(e))

    try:
        with open('homeapp.json', 'r') as json_file:
            params2 = json.load(json_file)
            json_file.close()
        
        params2[_ID] = _state 
        

    except  Exception as e3:
        print(str(e3))
    
    try:
        with open('homeapp.json', 'w') as json_file:
            json.dump(params2, json_file)
    except  Exception as e4:
        print(str(e4)) 

    return 'Test page under progress'

@app.route("/dummy", methods=['GET'])
def dummies():
    with open('homeapp.json') as js_file:
        d = json.load(js_file)
        #print ("New Json is: " + d["Level"])

    return jsonify(temp = d['Temperature'], hum = d['Humidity'])


@app.route('/')
def index():
    
    try:
        with open('homeapp.json', 'r') as _file:
            prm = json.load(_file)

    except  Exception as e3:
        print(str(e3))

    return render_template('homeapp.html', AC = prm['AC'],GS = prm['GS'],RF = prm['RF'],L1 = prm['L1'],L2 = prm['L2'])
 

if __name__ == '__main__':
    #app.secret_key = os.urandom(12)
    port = int(os.getenv('PORT', 5007))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
    #app.run(debug=True)
