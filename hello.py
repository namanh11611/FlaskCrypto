from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
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