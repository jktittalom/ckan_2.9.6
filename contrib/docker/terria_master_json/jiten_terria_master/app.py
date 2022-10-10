from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/')
def terriamasterjson():
    return [1,2,3]