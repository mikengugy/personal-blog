import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/mypersonalblog'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = 'Michael123'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'development':ProdConfig
}