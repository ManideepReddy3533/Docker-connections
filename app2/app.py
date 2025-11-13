from flask import Flask,jsonify,request
import requests

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"message":"Welcome to App 2!"})

@app.route('/call_app1')
def call_app1():
    try:
        res = requests.get('http://first_app_container:5000')
        return jsonify({"From App1": "App2 says " + res.json().get("message")})
    except Exception as e:
        data = {'error': str(e)}
        return jsonify(data), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
