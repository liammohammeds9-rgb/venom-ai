from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<html><body>CAPTIVE PORTAL <p>Your network is not secure</p></body></html>'
if __name__ == '__main__':
    app.run(host='0.0', port=8080)
