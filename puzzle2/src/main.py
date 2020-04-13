from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def default():
    return "Welcome to the Main Page"

@app.route("/api/email")
def email():
    emailJson = {
        "displayName": "Adam Sir",
        "emailAddress":"adam.sir@testproject.com"
    }
    return json.dumps(emailJson)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)