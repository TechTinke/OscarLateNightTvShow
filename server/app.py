import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Defer blueprint imports to avoid circular imports
def register_blueprints():
    from server.controllers.auth_controller import auth_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.appearance_controller import appearance_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

# Register blueprints after db is initialized
register_blueprints()

if __name__ == '__main__':
    app.run(debug=True)