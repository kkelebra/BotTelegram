from flask import Flask, request

app = Flask(__name__)

@app.route('/msm', methods=['POST'])
def msm():
    request_data = request.get_json()
    msm = request_data['msm']
    number_origin = request_data['number-origin']
    number_destination = request_data['number-destination']
    print(number_origin, "=>", number_destination)
    print("-" * 100)
    print(msm)
    print("#" * 100)
    return "Correct";

@app.route('/')
def hello_world():
    return 'Hello, World!'