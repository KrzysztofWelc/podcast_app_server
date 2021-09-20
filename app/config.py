import os
from dotenv import load_dotenv

load_dotenv('../.env')


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@postgre-db:5432/{}".format(
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_NAME'),
    )


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_TEST")
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
