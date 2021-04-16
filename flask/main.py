from os import urandom
from flask import Flask, jsonify

app = Flask(__name__)
app.secret_key = urandom(24)

@app.route('/')
def index():
	return jsonify({
    'hola': "mundo"
  })

if __name__ == '__main__':
	app.run(port=5010, debug=True)