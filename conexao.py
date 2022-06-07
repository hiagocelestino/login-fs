import os
import psycopg2

def get_conexao():
    conn = psycopg2.connect(
        host=os.environ.get("HOST"),
        database=os.environ.get("DATABASE"),
        user=os.environ.get("USER_DB"),
        password=os.environ.get("PASSWORD_DB")
    )
    return conn



