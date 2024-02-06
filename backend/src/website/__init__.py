from flask import Flask
from flask_cors import CORS

from .view.view_main import VIEW
from .login.login_main import LOGIN
from .upload.upload_main import UPLOAD


def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/website/": {"origins": "*", "allow_headers": ["Content-Type"]}})
    app.secret_key = 'key'
    
    app.register_blueprint(LOGIN, url_prefix='/login')
    app.register_blueprint(UPLOAD, url_prefix='/upload')
    app.register_blueprint(VIEW, url_prefix='/view')
    
    return app
