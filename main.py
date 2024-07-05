"""Biblioteca"""
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    """Funcion"""
    return render_template('base.html')
