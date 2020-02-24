import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev_database.db"


# class TestingConfig(BaseConfig):
#     """Testing configuration."""
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = "sqlite:///test_database.db"
#     PRESERVE_CONTEXT_ON_EXCEPTION = False


# # class ProductionConfig(BaseConfig):
#     """Production configuration."""
#     SECRET_KEY = os.getenv('SECRET_KEY')
#     DEBUG = False
#     # SQLALCHEMY_DATABASE_URI = 'postgresql:///writ'
#     print("NEED TO LOOKUP HEROKU database URI")
