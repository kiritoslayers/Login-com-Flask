import os
from pydoc import describe
import psycopg2
from dotenv import load_dotenv


# lendo as variáveis de ambiente
load_dotenv()
# pegando a variável de ambiente
DATABASE_URI = os.environ["URI"]


def row_to_dict(description, row):
    if row is None:
        return None
    d = {}
    for i in range(0, len(row)):
        d[description[i][0]] = row[i]
    return d


def fazer_login(user, password):
    # conectando com o banco
    db = psycopg2.connect(DATABASE_URI)
    with db.cursor() as cursor:
        # montando a query string
        query = f"""select users, password_hash from "Madarah".users where users = '{user}' and password_hash = '{password}'"""
        cursor.execute(query)
        description = cursor.description
        fetchone = cursor.fetchone()
        return row_to_dict(description, fetchone)


def registrar(user, password):
    # conectando com o banco
    db = psycopg2.connect(DATABASE_URI)
    with db.cursor() as cursor:
        # monta a query string
        query = f"""insert into "Madarah".users (users, password_hash) values ('{user}', '{password}')"""
        # executa a query
        cursor.execute(query)
        return db.commit()
