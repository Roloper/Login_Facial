from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id_usuario, nombre, correo, password, imagen_perfil=None,imagen_test=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.imagen_perfil = imagen_perfil

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
