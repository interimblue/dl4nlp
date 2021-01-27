from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from CG import CovidGenerator

app = Flask(__name__)
api = Api(app)

gpt = CovidGenerator()

class CovidGen(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task')

        args = parser.parse_args()
        answ = gpt.generate()

        return {'answer':'{}'.format(answ)}, 200

api.add_resource(CovidGen, '/covid')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

