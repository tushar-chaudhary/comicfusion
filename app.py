from flask import Flask
from routes import auth


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    auth.generate_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
