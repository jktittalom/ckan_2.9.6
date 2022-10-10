from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/')
def hello_world():
   return "Welcome Jiten!!"

@app.route('/hello')
def hello_world():
   return "hello world"
