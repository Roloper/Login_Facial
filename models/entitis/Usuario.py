from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):

    def __init__(self, id_usuario, nombre, correo, password, imagen_perfil):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.imagen_perfil = imagen_perfil

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)



class Vendedor(Usuario):

    def __init__(self, id_usuario, nombre, correo, password,imagen_perfil, imagen_test):
        super().__init__(id_usuario, nombre, correo, password, imagen_perfil)
        self.imagen_test = imagen_test


class Admin(Usuario):

    def __init__(self, id_usuario, nombre, correo, password, imagen_perfil):
        super().__init__(id_usuario, nombre, correo, password, imagen_perfil)
