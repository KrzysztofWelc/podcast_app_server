import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from py_yaml_fixtures.flask import PyYAMLFixtures
from dotenv import load_dotenv
from app.celery_tasks.celery_utils import init_celery
import pymysql

pymysql.install_as_MySQLdb()

load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()
fixtures = PyYAMLFixtures()
migrate = Migrate()
cors = CORS(resources={r"/api/*": {"origins": "*"}})


def create_app(config=None, **kwargs):
    app = Flask(__name__)

    if not config:
        app_settings = os.getenv("APP_SETTINGS", "app.config.DevelopmentConfig")
    else:
        app_settings = config

    app.config.from_object(app_settings)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config[
        "FLASK_MODELS_MODULE"
    ] = "app.models"  # where all of your model classes are imported
    app.config[
        "PY_YAML_FIXTURES_DIR"
    ] = "app/fixtures"  # where your fixtures file(s) live
    app.config[
        "PY_YAML_FIXTURES_COMMAND_NAME"
    ] = "import_fixtures"  # the name of the CLI command
    db.init_app(app)
    bcrypt.init_app(app)
    fixtures.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    if kwargs.get("celery_tasks"):
        init_celery(kwargs.get("celery_tasks"), app)

    from app.users.routes import users
    from app.podcasts.routes import podcasts
    from app.comments.routes import comments
    from app.search.routes import search

    app.register_blueprint(users, url_prefix="/api/users")
    app.register_blueprint(podcasts, url_prefix="/api/podcasts")
    app.register_blueprint(comments, url_prefix="/api/comments")
    app.register_blueprint(search, url_prefix="/api/search")

    return app
