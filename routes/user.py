# test file
from flask_restful import Resource


class UserRoute(Resource):
    def get(self):
        return {'code': 200, 'msg': 'ok', 'data': 'hello world!'}
