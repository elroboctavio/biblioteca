"""Biblioteca"""
import psycopg2
from flask import Flask, redirect, render_template, url_for, request
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
    # Conectar con la base de datos
    conexion = psycopg2.connect (
        database="Bliblioteca3A",
        user="postgres",
        password="tVE4QgrFP9rnEb",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libros_vistas''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursos y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():
    # Conectar con la base de datos
    conexion = psycopg2.connect (
        database="Bliblioteca3A",
        user="postgres",
        password="tVE4QgrFP9rnEb",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM autores_view''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursos y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)

@app.route('/pais')
def pais():
    # Conectar con la base de datos
    conexion = psycopg2.connect (
        database="Bliblioteca3A",
        user="postgres",
        password="tVE4QgrFP9rnEb",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM "Pais"''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursos y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('paises.html', datos=datos)


@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    # Conectar con la base de datos
    conexion = psycopg2.connect (
        database="Bliblioteca3A",
        user="postgres",
        password="tVE4QgrFP9rnEb",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # borrar un registro con el id_pais seleccionado
    cursor.execute('''DELETE  FROM "Pais" WHERE id_pais=%s''', (id_pais,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))

@app.route('/update1_pais/<int:id_pais>', methods=['GET','POST'])
def update1_pais(id_pais):
        # Conectar con la base de datos
    conexion = psycopg2.connect (
        database="Bliblioteca3A",
        user="postgres",
        password="tVE4QgrFP9rnEb",
        host="localhost",
        port="5432"
    )
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # recuperar un registro con el id_pais seleccionado
    cursor.execute('''SELECT * FROM "Pais" WHERE id_pais=%s''', (id_pais,))
    datos=cursor.fetchall()
    # id_pais= request.form['id_pais']
    # nombre = request.form['nombre']
    # datos ={
    #     'id_pais':id_pais,
    #     'nombre':nombre
    # }
    cursor.close()
    conexion.close()
    return render_template('editar_pais.html', datos=datos)
