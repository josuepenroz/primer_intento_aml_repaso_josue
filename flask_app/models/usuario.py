#TODAS LAS CLASES INPORTAR MYSQLCONNECTION

from flask_app.config.mysqlconnection import connectToMySQL

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
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW() NOW())"
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
            usuario.append(cls(usuario))
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
    #