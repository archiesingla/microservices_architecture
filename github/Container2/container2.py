from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

#restricting only POST request, and adding calculate as a path in URL. 
@app.route('/calculate', methods=['POST'])

def coreLogic():
    #creating the request
    data = request.json
    #defining the path to locate file in volume
    file_absolute_path = '/Archie_PV_dir/' + data['file']
    product_name = data['product']
    file_name = data['file']

    try:
        csv_content = pd.read_csv(file_absolute_path)

        #the data of file should have products and amount and sepereated by comma
        if 'product' not in csv_content.columns or 'amount' not in csv_content.columns:
            return jsonify({"file": file_name, "error": "Input file not in CSV format."})

        sum=0
        product_list = csv_content['product'].tolist()
        amount_list = csv_content['amount'].tolist()

        #parse each product item and match with the give one.
        if(product_name in product_list):
            for items in range(len(product_list)):
                #when it matches then add the amount and get sum
                if(product_name == product_list[items]):
                    sum = sum + amount_list[items]
            print(sum)
            return jsonify({"file": file_name, "sum": sum})
        else:
            #if product mentioned is not in the list then give error
            return jsonify({"file": file_name, "error": "given item is not in the file"})

    #checking the CSV format
    except pd.errors.ParserError:
        return jsonify({"file": file_name, "error": "Input file not in CSV format."})
    # if file is not found in the given volume location
    except FileNotFoundError:
        return jsonify({"file": None, "error": "File not found."})
    except Exception as e:
        return jsonify({"file": file_name, "error": str(e)})


#listining on 7000 port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)







