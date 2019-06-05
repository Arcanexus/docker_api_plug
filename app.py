#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///storage.db')
app = Flask(__name__)
api = Api(app)


class Requests(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from http_input_logs") # This line performs query and returns json result
        return query.cursor.fetchall() 
    
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        
        http_request = request.get_json(force=True)
        
        query = conn.execute("insert into http_input_logs values('{0}')".format(dumps(http_request)))
        return {'status':'success'}

    
api.add_resource(Requests, '/') # Route_1

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port='5002')
