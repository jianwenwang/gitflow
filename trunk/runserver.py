from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return json.dumps({'code':10,'data':[],'msg':'hello world!'})
	

@app.route('/queryUser')
def query_user():
    return json.dumps([])

	
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
