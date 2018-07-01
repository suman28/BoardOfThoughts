# from flask import Flask, request
# from flask_cors import CORS, cross_origin
# from flask_restful import Resource, Api
# from json import dumps
# from flask_jsonpify import jsonify

# from flask_sqlalchemy import SQLAlchemy



# # from pyodbc import *


# # engine = create_engine('mssql+pyodbc://{db_user}:{db_password}@{db_url}/{db_name}')

# app = Flask(__name__, instance_relative_config=True)
# api = Api(app)

# # app.config.from_object('config')
# # app.config.from_pyfile('config.py')

# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://sa:Passw)rd@http://winsumank28:5432/RetroBoard"

# db = SQLAlchemy(app)

# CORS(app)

# class Engine(db.Model):

#     # Columns

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     title = db.Column(db.String(128))

#     thrust = db.Column(db.Integer, default=0)

# @app.route("/")
# def hello():
#     return jsonify({'text':'Hello World!'})

# class Employees(Resource):
#     def get(self):
#         return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         print('Employee id:' + employee_id)
#         result = {'data': {'id':1, 'name':'Balram'}}
#         return jsonify(result)       


# api.add_resource(Employees, '/employees') # Route_1
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


# if __name__ == '__main__':
#      app.run(port=5002)