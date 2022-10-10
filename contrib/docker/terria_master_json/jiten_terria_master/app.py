from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/')
def terriamasterjson():
	print("Welcome Jiten!!!")
    return "ok Jiten"


@app.route('/test')
def test():
	print("Test Welcome Jiten!!!")
    return "Test Ok Jiten"
