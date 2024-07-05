"""Biblioteca"""
import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

app=Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    """Funcion"""
    return render_template('base.html')

@app.route('/libros')
def libros():
    """Conectar con la base de datos"""
    conexion = psycopg2.connect(
        database = "Blblioteca3A",
        user = "postgres",
        password ="tVE4QgrFP9rnEb",
        host="localhost",
        port="5432"
    )
    """crear un cursor  (objeto para recorrer tablas)"""
    cursor= conexion.cursor()
    """ejecutar una consulta en postgreSQL que recupera toda la informacion de los libros"""
    cursor.execute('''SELECT * FROM "Libro"''')
    """recupera información"""
    datos=cursor.fetchall()
    """cerrar cursor y conexion a la base de datos"""
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)
