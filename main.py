"""Biblioteca"""
import psycopg2
from flask import Flask, redirect, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
import db


app=Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    """Funcion"""
    return render_template('base.html')

@app.errorhandler(404)
def error404():
    return render_template

@app.route('/libros')
def libros():
    conn = db.conectar()
    # Conectar con la base de datos
    cursor = conn.cursor()
    # ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libros_vistas''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursos y conexion a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM autores_view''')
    datos = cursor.fetchall()
    cursor.close()
    db.desconectar(conn)
    return render_template('autores.html', datos=datos)

@app.route('/pais')
def pais():
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "Pais" ORDER BY id_pais''')
    datos = cursor.fetchall()
    cursor.close()
    db.desconectar(conn)
    return render_template('paises.html', datos=datos)


@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('''DELETE  FROM "Pais" WHERE id_pais=%s''', (id_pais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))

@app.route('/update1_pais/<int:id_pais>', methods=['POST'])
def update1_pais(id_pais):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "Pais" WHERE id_pais=%s''', (id_pais,))
    datos=cursor.fetchall()
    cursor.close()
    db.desconectar(conn)
    return render_template('editar_pais.html', datos=datos)

@app.route('/update2_pais/<int:id_pais>', methods=['POST'])
def update2_pais(id_pais):
    nombre = request.form['nombre']
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('''UPDATE "Pais" SET nombre=%s WHERE id_pais=%s''', (nombre,id_pais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))
