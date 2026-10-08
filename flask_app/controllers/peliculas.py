from flask_app import app
from flask import render_template,request,session,flash

@app.route("/cine")
def pelicula():
    return render_template("peliculas.html")
def nueva_pelicula():
    datos = {
        "nombre":request.form.get['nombre'],
        "apellido":request.form.get['apellido'],
        "email":request.form.get['email'],
        "password":request.form.get['password']
    }
    
    Usuario.save(datos)
    return render_template("cine.html", usuario=datos)