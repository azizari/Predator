from flask import Flask, request
from flask_cors import CORS
import json
from ml import funcs

app = Flask(__name__)
CORS(app)

sick_model = "xy"



@app.route("/copypaste", methods=['GET', 'POST'])
def template_test():
    
    p = request.data
    pj = json.loads(p)['postData']
    fj = json.dumps(funcs(pj))

    return fj#'test str'






if __name__ == '__main__':
    app.run(debug=True)