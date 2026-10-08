from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt #Importamos Bcrypt

bcrypt = Bcrypt(app)



@app.route("/")
def inicio():
    return render_template("index.html")

#regitro
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    
    #para agregar un usuario lo primero que debo hacer es 
    #recuperar la informacion desde el formulario
    # %(nombre)s, %(apellido)s, %(email)s, %(password)s
    if not Usuario.validar_usuario(request.form):
        
        
        
        flash("El correo es obligatorio ", "correo")
    #return redirect("/")
    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])
    datos_usuarios_registro = {
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "email":request.form['email'],
        "password":request.form['password'],
        'password':pass_hasheado
    }
    
    Usuario.save(datos_usuarios_registro)
    return render_template("cine.html", usuario=datos_usuarios_registro)
    nuevo_id = Usuario.save()

@app.route("/cine")
def cine():
    return render_template("cine.html")
                 
#proyeccion de rutas 
