from decouple import config  # trabaja con variables de entorno (.env)

class Config:
    MYSQL_HOST = config('MYSQL_HOST')
    MYSQL_USER = config('MYSQL_USER')
    MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    MYSQL_DB = config('MYSQL_DB')
    SECRET_KEY = config('SECRET_KEY')
    
    


# cada vez que se realiza un cambio el servidor se refresca solo
class DevelopmentConfig(Config):
    DEBUG = True                    # parametro de depuracion activo


config = {
    'development': DevelopmentConfig
}

