from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta segura

    with app.app_context():
        # Importar las rutas
        from . import routes

    return app