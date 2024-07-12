from flask_restful import Api
from handler import auth

prefix = '/auth'


def generate_routes(app):
    api = Api(app)

    api.add_resource(auth.Register,
                     "{}/register".format(prefix))
    api.add_resource(auth.Login,
                     "{}/login".format(prefix))
