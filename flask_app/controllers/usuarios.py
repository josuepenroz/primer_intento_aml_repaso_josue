from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.usuario import Usuario


@app.route("/")
def inicio():
    return render_template("index.html")

#regitro
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre":request.form.get('nombre'),
        "apellido":request.form.get('apellido'),
        "email":request.form.get('email'),
        "password":request.form.get('password')
    }
    
    Usuario.save(datos)
    return render_template("cine.html", usuario=datos)


@app.route("/cine")
def cine():
    return render_template("cine.html")