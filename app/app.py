from flask import Flask, request, jsonify

from database import Database


#flask db var
app = Flask(__name__)

db = Database()


@app.route('/')
def index():
    return "<h1>Hello Flask</h1>"

@app.route('/users', methods=['GET'])
def get_users():
    users = db.get_users() 
    return jsonify(users)

@app.route('/users/<int:uid>', methods=['GET'])
def get_user(uid):
    user = db.get_user(uid)
    if user:
        return jsonify(user)
    elif not user:
        return jsonify({"msg":"Users not exits"}), 404

@app.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid, name, age):
    pass

@app.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    pass

if __name__ == '__main__': 
   app.run(debug=True)