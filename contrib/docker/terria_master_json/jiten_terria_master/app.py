from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/')
def index():
   return "Welcome Jiten!!"

@app.route('/hello')
def hello():
   return "hello world"
