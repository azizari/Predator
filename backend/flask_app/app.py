from flask import Flask, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

sick_model = "xy"



@app.route("/copypaste", methods=['GET', 'POST'])
def template_test():
    
    p = request.data
    pj = json.loads(p)['postData']*900


    return pj#'test str'






if __name__ == '__main__':
    app.run(debug=True)