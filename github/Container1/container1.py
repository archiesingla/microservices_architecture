from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/store-file', methods=['POST'])
def store_file():
    if not request.is_json:
        return jsonify({"file": None, "error": "Request must be JSON."})
    
    data = request.json
    if not data or 'file' not in data or not data['file']:
        return jsonify({"file": None, "error": "Invalid JSON input."})
    
    file_name = data['file']
    file_path = '/Archie_PV_dir/' + data['file']
    file_data = data.get('data', '')
    
    try:
        with open(file_path, 'w') as file:
            file.write(file_data.replace(" ", ""))  # Remove unnecessary spaces
        return jsonify({"file": file_name, "message": "Success."})
    except Exception as e:
        return jsonify({"file": file_name, "error": "Error while storing the file to the storage."})


#restricting only POST request, and adding calculate as a path in URL. 
@app.route('/calculate', methods=['POST'])
def filterAndVerify():

    #check if the data is in json format
    if not request.is_json:
        return jsonify({"file": None, "error": "Request must be JSON."})

    #creating the request
    data = request.json

    """
    checks 3 things together:
    1. if data is empty, 
    2. if file key is missing in the data, 
    3. if the value of file key is missing

    If above conditions are true, then return the error of Invalid JSON input.
    """
    if not data or 'file' not in data or not data['file'] :
        return jsonify({"file": None, "error": "Invalid JSON input."})

    #fetching the file name from input
    file_name = data['file']
    file_absolute_path = '/Archie_PV_dir/' + data['file']
    
    #check if file exists in the volume directory
    if not os.path.isfile(file_absolute_path):
        return jsonify({"file": file_name, "error": "File not found."})

    #if everything is correct then pass to container 2:
    CONTAINER_2_URL = "http://localhost:7000/calculate"
    response = requests.post(CONTAINER_2_URL, json=data)
    return jsonify(response.json())

#listining on 6000 port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)







