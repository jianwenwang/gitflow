from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return json.dumps({'code':10,'data':[],'msg':'hello world!'})

@app.route('/getUser')
def get_user():
    return json.dumps({'id':1,'name':'耿达达'})
	
if __name__ == '__main__':
    print('start run!')
    app.run('0.0.0.0', 5000, debug=True)
	print('start succeed!')
