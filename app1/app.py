from flask import Flask,jsonify,request
import requests
app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"message":"Welcome to App 1!"})
@app.route('/call_app2')
def call_app2():
    try:
        res = requests.get('http://second_app_container:5001')
        return jsonify({"From App2": "App1 says"+ res.json().get("message")})
    except Exception as e:
        data = {'error': str(e)}
        return jsonify(data), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
