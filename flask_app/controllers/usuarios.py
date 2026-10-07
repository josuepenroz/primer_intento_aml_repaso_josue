from flask_app import app
from flask import render_template


@app.route("/")
def inicio():
    return render_template("index.html")

#regitro
@app.route("/crear_usuario")
def crear_usuario():
    return