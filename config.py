class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    # DEBUG = True
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
