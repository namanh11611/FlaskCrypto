from flask import Flask, jsonify, request
from pyngrok import ngrok

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

url = ngrok.connect(5000).public_url
print('Henzy Tunnel URL:', url)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/memories')
def welcome():
    args = request.args

    if "learner_id" in args:
        learner_id = args["learner_id"]
        if learner_id == "anhnn2":
            return {"history":[{"items":[{"session_name":"02","history_created_time":"'2021-01-02 10:23:65","checkin_learner_status":"yes"},{"session_name":"03","history_created_time":"'2021-01-05 10:20:43","checkin_learner_status":"no"},{"session_name":"04","history_created_time":"'2021-01-07 10:21:12","checkin_learner_status":"rejected"}],"file_id":"1230","file_name":"Địa Lý Cơ sở địa lý tự nhiên 1","class_name":"GEOG 127G-K69SP Địa.1_LT"},{"items":[{"session_name":"02","history_created_time":"'2021-01-02 10:23:65","checkin_learner_status":"yes"},{"session_name":"03","history_created_time":"'2021-01-05 10:20:43","checkin_learner_status":"no"},{"session_name":"04","history_created_time":"'2021-01-07 10:21:12","checkin_learner_status":"rejected"}],"file_id":"124","file_name":"Địa Lý Cơ sở địa lý tự nhiên 2","class_name":"GEOG 127G-K69SP Địa.2_LT"}]}

    return 'Welcome page'

@app.route('/me')
def me():
    return jsonify(
        name="Nam Anh",
        age=24
    )

@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify(users)

def get_all_users():
    # return [Person("Nam Anh", 25), Person("Quynh Hoa", 25), Person("Viet Ha", 21)]
    return [
        {
            "name": "Nam Anh",
            "age": 25
        },
        {
            "name": "Nam Anh",
            "age": 25
        },
        {
            "name": "Nam Anh",
            "age": 25
        }
    ]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age