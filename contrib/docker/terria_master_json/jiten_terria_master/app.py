from pathlib import Path
import json
import os

from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/')
def hello_world():
   return "Welcome Jiten!!"

@app.route('/test')
def hello_world():
	print("Testing indentaion!!!")
   return "hello world"
