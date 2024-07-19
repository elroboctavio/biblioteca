import psycopg2
from psycopg2 import pool

#Crear un pool de conexiones 
connection_pool = pool.SimpleConnectionPool(
    1,20,
    database="Bliblioteca3A",
    user="postgres",
    password="tVE4QgrFP9rnEb",
    host="localhost",
    port="5432"
)

def conectar():
    return connection_pool.getconn()

def desconectar(conn):
    return connection_pool.getconn()
    connection_pool.putconn(conn)