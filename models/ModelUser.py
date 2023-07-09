from entities.Usuario import User, Vendedor, Admin

class ModelUser():
    @classmethod
    def login(cls, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, nombre, correo, password, imagen_perfil
                     FROM usuario where correo = %s"""
            cursor.execute(sql, (user.correo,))
            row = cursor.fetchone()
            if row is not None:
                return User(
                    row[0], row[1], row[2], User.check_password(row[3], user.password), row[4]
                )
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(cls, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, nombre, correo, password, imagen_perfil
                     FROM usuario where id_usuario = %s"""
            cursor.execute(sql, (id_usuario,))
            row = cursor.fetchone()
            if row is not None:
                return User(
                    row[0], row[1], row[2], None, row[3]
                )
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def register(cls, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO usuario(nombre, correo, password, imagen_perfil)
                     VALUES(%s, %s, %s, %s)"""
            cursor.execute(sql, (
                user.nombre, user.correo, user.password, user.imagen_perfil
            ))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get_all_users(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, nombre, correo, password, imagen_perfil
                     FROM usuario"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append({
                    'id_usuario': row[0],
                    'nombre': row[1],
                    'correo': row[2],
                    'password': row[3],
                    'imagen_perfil': row[4]
                })
            return users
        except Exception as ex:
            raise Exception(ex)

class ModelVendedor(ModelUser):
    @classmethod
    def register(cls, db, vendedor):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO usuario(nombre, correo, password, imagen_perfil, imagen_test)
                     VALUES(%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                vendedor.nombre, vendedor.correo, vendedor.password, vendedor.imagen_perfil, vendedor.imagen_test
            ))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

class ModelAdmin(ModelUser):
    pass
