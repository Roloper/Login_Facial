from entitis.Usuario import Usuario, Vendedor, Admin

class ModelVendedor:

    @classmethod
    def register(cls, db, vendedor):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO Vendedor (id_usuario, imagen_test) VALUES ({}, '{}')".format(
                vendedor.id_usuario, vendedor.imagen_test)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)


class ModelAdmin:

    @classmethod
    def register(cls, db, admin):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO Admin (id_usuario) VALUES ({})".format(
                admin.id_usuario)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

class ModelUser:

    @classmethod
    def login(cls, db, correo, password):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, nombre, correo, password, imagen_perfil FROM Usuario 
                    WHERE correo = '{}'""".format(correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None and Usuario.check_password(row[3], password):
                usuario = Usuario(row[0], row[1], row[2], row[4])
                if isinstance(usuario, Vendedor):
                    model_vendedor = ModelVendedor()
                    model_vendedor.login(db, usuario)
                elif isinstance(usuario, Admin):
                    model_admin = ModelAdmin()
                    model_admin.login(db, usuario)
                return usuario
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            if isinstance(usuario, Vendedor):
                sql = "DELETE FROM Vendedor WHERE id_usuario = {}".format(usuario.id_usuario)
            elif isinstance(usuario, Admin):
                sql = "DELETE FROM Admin WHERE id_usuario = {}".format(usuario.id_usuario)
            else:
                sql = "DELETE FROM Usuario WHERE id_usuario = {}".format(usuario.id_usuario)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
