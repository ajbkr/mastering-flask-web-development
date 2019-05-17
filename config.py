class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    # DEBUG = True
    debug = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mfwd:mfwd@127.0.0.1:5432/mfwd'
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
