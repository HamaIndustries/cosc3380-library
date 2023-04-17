import psycopg2

from database.connection_secret import conn_info

def get_conn():
    return psycopg2.connect(**conn_info)
