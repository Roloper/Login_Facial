from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id_usuario, nombre, correo, password,admin, imagen_perfil=None,imagen_test=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.admin = admin
        self.imagen_perfil = imagen_perfil
        self.imagen_test = imagen_test
    
    def get_id(self):
        return str(self.id_usuario)
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
