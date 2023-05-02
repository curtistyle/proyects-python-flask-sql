import psycopg2                    # conector
from psycopg2 import DatabaseError # controla los errores de la base de datos
from decouple import config        # me permite obtener las variables de entorno para el nombre de usuario, password, servidor y db

def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex