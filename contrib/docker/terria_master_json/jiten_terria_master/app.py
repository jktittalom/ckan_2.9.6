from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/')
def terriamasterjson():
	print("Welcome Jiten!!!")
	return "ok"

@app.route('/hello')
def hello_world():
   return "hello world"
