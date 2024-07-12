from flask_restful import Resource, output_json
from services.auth import AuthService

service = AuthService()


class Register(Resource):
    def get(self):
        service.register()
        return output_json(data={"code": 200}, code=200)


class Login(Resource):
    def get(self):
        service.login()
        return output_json(data={"code": 200}, code=200)
