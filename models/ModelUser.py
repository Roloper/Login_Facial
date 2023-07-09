from models.entities.Usuario import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, Nombre, correo, contrasena, 
                    admin, imagen_perfil, imagen_test
                     FROM usuario where correo = '{}' """.format(user.correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], User.check_password(row[3], user.a_password), row[4], row[5],
                            row[6])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, Nombre, correo,
                    admin, imagen_perfil, imagen_test
                     FROM usuario where id_usuario = '{}' """.format(id_usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], None, row[3], row[4], row[5])

            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def register(cls, db, user):
        try:
            cursor = db.connection.cursor()

            sql = """INSERT INTO usuario(a_name, a_username, a_password, a_email, a_descripcion, a_celular, a_ubicacion, a_imagenperfil) 
                     VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                user.a_name, user.a_username, user.a_password, user.a_email, user.a_descripcion, user.a_celular,
                user.a_ubicacion, user.a_imagenperfil)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_users(cls, db):
        try:
            cursor = db.connection.cursor()

            sql = """SELECT id_usuario, Nombre, correo,
                    admin, imagen_perfil, imagen_test
                     FROM usuario """
            cursor.execute(sql)
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append({
                    'id_usuario': row[0],
                    'Nombre': row[1],
                    'correo': row[2],
                    'admin': row[3],
                    'imagen_perfil': row[4],
                    'imagen_test': row[5],
                })
            return users
        except Exception as ex:
            raise Exception(ex)