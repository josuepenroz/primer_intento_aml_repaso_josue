#TODAS LAS CLASES INPORTAR MYSQLCONNECTION

from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
class Usuario:
    #metodo constructor 
    def __init__(self,data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
    #para guardad un 1 registro 
    @classmethod
    def save(cls,data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW())"
        return connectToMySQL('cinepedia').query_db(query,data)
        #metodos para ver todos los registros
    
    @classmethod
    def get_all(cls):
        query = "SELECT  * FROM usuarios"
        usuarios_en_bd = connectToMySQL('cinepedia').query_db(query)
       #lista vacia de usuarios
        usuarios = []
        for usuario in usuarios_en_bd:
            #voy a crear una instancia de la clase Usuario al final de la lista usuarios
            usuarios.append(cls(usuario))
        return usuarios 
    @classmethod
    def get_one(cls,datos):
            query = "SELECT * FROM usuarios WHERE id = %(id)s;"
            usuarios_en_db = connectToMySQL('cinepedia').query_db(query,datos)
    
            return cls(usuarios_en_db[0])
    @classmethod
    def update(cls, datos):
            query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, password=%(password)s WHERE id = %(id)s;"
            return connectToMySQL('cinepedia').query_db(query, datos)
    @classmethod
    def delete(cls, datos):
            query = "DELETE FROM usuarios WHERE id = %(id)s;"
            return connectToMySQL('cinepedia').query_db(query, datos)
    
    #metodo para ver 1 registro
    #metodo para editar registro
    #Usuamos metodo estaticp para validar los formularios
    @classmethod
    def get_by_email(cls,datos):
        query   = "SELECT * FROM usuarios WHERE email=%(email)s"    
        usuarios_en_db = connectToMySQL('cinepedia').query_db(query,datos)
        return cls(usuarios_en_db[0])
    
    
    
    @staticmethod

    def validar_usuario( usuario ):
        #por cada validacion que yo tenga voy a un if
       es_valido = True

       #Revisa si el campo coincide con el patrón

       if not EMAIL_REGEX.match(usuario['email']):

           flash("E-mail inválido")

           es_valido = False
       if len(usuario['nombre']) <= 2:
            flash("nombre de usuario necesita almenos 2 caracteres")
            es_valido = False
            #falta validacion de contraseña = confirmar contraseña
       if not Usuario['password'] == usuario["password_conf"]:
            flash 
            return es_valido
       if not Usuario.get_by_email({'email':usuario['email']}):
           flash('el correo no se encuentra disponible')
           es_valido = False
           return es_valido
       @staticmethod
       def  validar_login(usuario):
           es_valido=True
           if not Usuario.get_by_email({'email':usuario['email']}):
               flash('el correo no se encuentra el la base de datos')
               
       
        
