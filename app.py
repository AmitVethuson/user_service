# user_service.py

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
    }

#get all users
@app.route('/user', methods=['GET'])
def getAllUsers():
    return users

#get secific user
@app.route('/user/<id>' ,methods=['GET'])
def user(id):
    if id in users:
        user_info = users.get(id, {})
        return jsonify(user_info)
    else:
        return {'error': 'User Does Not Exist'}

#create a new user
@app.route('/user',methods=['POST'])
def create_user():
    newId = (len(users)+1)
    new_user = {
        str(newId ):  { 'name':request.json['name'], 'email':request.json["email"]}
            }
    users.update(new_user)
    return new_user

#Update user
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):    
    if id in users:
        updatedUser = {'name':request.json['name'] ,'email': request.json['email']}
        users.update({id:updatedUser})
        return updatedUser
    else:
        return {'error':'User Not Found'}
    
    
#delete user
@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return users
    else:
       return {'error': 'User Does Not Exist'}




if __name__ == '__main__':
  
    app.run(debug=True)
    
