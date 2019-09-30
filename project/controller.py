from flask import jsonify
from project import app
from project.models import User

@app.route('/')
def hello():
    return f'Hello, World!'


#user = {'name':'Tugce','pin':12345,'balance':1000}
#users = [{'name':'John','pin':12345,'balance':1000}, {'name':'Jane','pin':12345,'balance':2000}]

@app.route('/users')
def getUsers():
    xxxx = User.query.all()
    return jsonify(xxxx[0].name)