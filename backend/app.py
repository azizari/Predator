from flask import Flask, request
from flask_cors import CORS
import json
from predator import Predator
#from ml import funcs

# test
predator = Predator()

app = Flask(__name__)
CORS(app)


@app.route("/copypaste", methods=['GET', 'POST'])
def template_test():
    
    p = request.data
    pj = json.loads(p)['postData']
    predator.crunch(pj, n_lags=5, n_steps=5)
    vomit = predator.vomit()
    #fj = json.dumps(funcs(pj))

    return vomit






if __name__ == '__main__':
    app.run(debug=True)