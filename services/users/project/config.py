# services/users/project/config.py


import os  # new


class BaseConfig:
    """Configuracion Base"""

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_key"  # nuevo
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BCRYPT_LOG_ROUNDS = 13  #nuevo


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # new
    DEBUG_TB_ENABLED = True
    BCRYPT_LOG_ROUNDS = 4  # nuevo


class TestingConfig(BaseConfig):
    """Configuracion de Testing"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
    BCRYPT_LOG_ROUNDS = 4  # nuevo


class ProductionConfig(BaseConfig):
    """Configuracion de Production"""
    DEBUG = False  # nuevo
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # nuevo
