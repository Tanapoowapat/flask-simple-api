from flask import Flask, request, jsonify

from database import Database


#flask db var
app = Flask(__name__)

db = Database()


@app.route('/')
def index():
    return "<h1>Hello Flask</h1>"

@app.route('/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    db.create_user(data['uid'], data['name'], data['age'])
    uid = data['uid']
    return jsonify({"message" : "User has been create", "uid" : uid}),201

@app.route('/users/', methods=['GET'])
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
def update_user(uid):
    user = get_user(uid)
    data = request.get_json()
    if user:
        db.update(uid, data['name'], data['age'])
        return jsonify({'msg': 'User Update'}),200
    if not user:
        return jsonify({'msg': 'User not found!'}),404
    

@app.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    user = get_user(uid)
    
    if user:
        db.delete_user(uid)
        return jsonify({'msg': 'User Delete'}),200
    if not user:
        return jsonify({'msg': 'User not Found'}),404

if __name__ == '__main__': 
   app.run(debug=True)