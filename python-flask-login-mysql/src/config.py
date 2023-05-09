class Config:
    SECRET_KEY = 'secretkey'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOT = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'flask_login'
    
config={
    'development' : DevelopmentConfig
}

    