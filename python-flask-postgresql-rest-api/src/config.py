from decouple import config  # trabaja con variables de entorno (.env)

class Config:
    SECRET_KEY = config('SECRET_KEY')


# cada vez que se realiza un cambio el servidor se refresca solo
class DevelopmentConfig(Config):
    DEBUG = True                    # parametro de depuracion activo


config = {
    'development': DevelopmentConfig
}
