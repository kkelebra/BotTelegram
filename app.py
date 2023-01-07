from flask import Flask, request

app = Flask(__name__)

@app.route('/msm', methods=['POST'])
def msm():
    request_data = request.get_json()
    msm = request_data['msm']
    print(msm);
    print("#" * 100)
    return "Correct";

@app.route('/')
def hello_world():
    return 'Hello, World!'