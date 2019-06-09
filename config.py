class Config(object):
    pass


class ProdConfig(Config):
    pass
    # SECRET_KEY = b'lx\x11\x16K\xbc=\xb9K\xdaN|\x89\xe4\x00\x1c!\xe3\x9c\xa2g\xb1\x10"'


class DevConfig(Config):
    # DEBUG = True
    debug = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mfwd:mfwd@127.0.0.1:5432/mfwd' # noqa E501
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = b'v\xadv9\xf0\x00\x8b@Wu\xfd\x05q\xed\xe4\x16\x97\xd7dI\xa9\tt\xb5'
