from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.dialects.mssql import pymssql

# engine = create_engine('mssql+pyodbc://{db_user}:{db_password}@{db_url}/{db_name}')

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

# app.config.from_object('config')
# app.config.from_pyfile('config.py')

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://sa:Passw)rd@10.181.214.44/RetroBoard"

db = SQLAlchemy(app)

CORS(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        # return '<Employee %r>' % self.username
        self.username = username
        self.email = email

    @property
    def serialize(self):
       return {
           'id'         : self.id,
           'username'   : self.username,
           'email'      : self.email
       }


@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

class Employees(Resource):
    def get(self):
        return jsonify(json_list=[i.serialize for i in Employee.query.all()])
        # return jsonify(Employee.query.all())
        # return {'employees': [{'id':1, 'name':'suman'},{'id':2, 'name':'siva'}]} 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'suman'}}
        return jsonify(result)       


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port=5002)