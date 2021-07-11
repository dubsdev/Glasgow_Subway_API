from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
all_stations = [{'Name': 'Bridge', 'Location': 'Bridge Street'}, {'Name': 'Ibrox', 'Location': 'Some street'}]

class Welcome(Resource):
    def get(self):
        return jsonify({'Message': 'Welcome to the Glasgow Subway API'})

class Stations(Resource):
    def get(self):
        return jsonify(all_stations)


api.add_resource(Welcome, '/')
api.add_resource(Stations, '/stations')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)

