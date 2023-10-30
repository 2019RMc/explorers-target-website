from flask import Flask, render_template, jsonify

app = Flask(__name__)

SHOOTERS = [
  {
    'id': 1,
    'name': 'Ross Walden',
    'sid': '33697',
    'class': 'FSA',    
  },
  {
    'id': 2,
    'name': 'Andrew Finch',
    'sid': '43697',
    'class': 'TR',    
  },
  {
    'id': 3,
    'name': 'Christopher Bromham',
    'sid': '53697',
    'class': 'TR',    
  }
]

@app.route('/')
def hello_world():
    return render_template('home.html',
                           shooters=SHOOTERS,
                          club='Explorers Rifle Club')

@app.route('/api/shooters')
def list_shooters():
    return jsonify(SHOOTERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) #port=8080