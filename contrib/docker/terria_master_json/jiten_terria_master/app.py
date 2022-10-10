from pathlib import Path
import json
import os


from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/')
def index():
   return "Welcome Jiten!!"

@app.route('/hello')
def hello():
   return "hello world"

@app.route('/test')
def test():
    print("test Welcome!!!")
    hpath = Path.home()
    cpath = Path.cwd()
    return "hello test cpath: {}, home: {}".format(cpath, hpath)