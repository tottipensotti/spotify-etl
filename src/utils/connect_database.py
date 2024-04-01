import psycopg2
from config import load_db_config

def connect(config):
    """ Connect to the PostgreSQL database server"""
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_db_config()
    connect(config)