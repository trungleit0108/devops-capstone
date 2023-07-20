from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25},
    {"id": 3, "name": "Bob Johnson", "age": 35}
]

@app.route('/')
def index():
    return 'You can route to /users to see list of user demo. Thanks!'

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
