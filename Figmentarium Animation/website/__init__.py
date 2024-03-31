from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="static")
    app.config['SECRET_KEY'] = 'oink'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app


