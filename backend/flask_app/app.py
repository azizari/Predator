from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)





@app.route("/copypaste", method=['POST'])
def template_test():
    
    
    
    return 'test str'






if __name__ == '__main__':
    app.run(debug=True)