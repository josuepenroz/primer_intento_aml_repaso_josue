#TODAS LAS CLASES INPORTAR MYSQLCONNECTION

from flask_app.config.mysqlconnection import connectToMySQL

class pelicula:
    #metodo constructor 
    def __init__(self,data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.director = data.get('director')
        self.fecha_estreno = data.get('pecha_estreno')
        self.sinopsis = data.get('sinopsis')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.usuario_id = data.get('usuario_id')
    #para guardad un 1 registro 
    @classmethod
    def save(cls,data):
        query = "INSERT INTO peliculas (nombre, director, fecha_estreno, sinopsis, created_at, updated_at,usuario_id) VALUES (%(nombre)s, %(director)s, %(fecha_estreno)s, %(sinopsis)s,NOW() NOW(),%(usuario_id)s )"
        return connectToMySQL('cinepedia').query_db(query,data)
        #metodos para ver todos los registros
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM peliculas"
        peliculas_en_db = connectToMySQL('cinepedia').query_db(query)
       #lista vacia de usuarios
        peliculas = []
        for pelicula in peliculas_en_db:
            #voy a crear una instancia de la clase Usuario al final de la lista usuarios
            peliculas.append(cls(pelicula))
        return pelicula 
    
    @classmethod
    def get_one(cls,datos):
            query = "SELECT * FROM peliculas WHERE id = %(id)s;"
            peliculas_en_db = connectToMySQL('cinepedia').query_db(query,datos)
    
            return cls(peliculas_en_db[0])
    @classmethod
    def update(cls, datos):
            query = "UPDATE peliculas SET nombre=%(nombre)s, director=%(director)s, fecha_estreno=%(fecha_estreno)s, sinopsis=%(sinopsis)s, %(usuario_id)s    WHERE id = %(id)s;"
            return connectToMySQL('cinepedia').query_db(query, datos)
    @classmethod
    def delete(cls, datos):
            query = "DELETE FROM peliculas WHERE id = %(id)s;"
            return connectToMySQL('cinepedia').query_db(query, datos)
    
    #metodo para ver 1 registro
    #metodo para editar registro
    #