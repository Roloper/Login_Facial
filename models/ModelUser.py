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
                return User(row[0], row[1], row[2], User.check_password(row[3], user.password), row[4], row[5],
                            row[6])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, a_name, a_username, a_email,
                    a_descripcion, a_celular, a_ubicacion, a_imagenperfil 
                     FROM usuario where id_usuario = '{}' """.format(id_usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], None, row[3], row[4], row[5], row[6], row[7])

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
    def enviar_solicitud(cls, db, user_id, connection_id):
        try:
            cursor = db.connection.cursor()
            # Verificar si ya existe una solicitud de conexión pendiente o aceptada entre los usuarios
            sql = """SELECT COUNT(*) FROM user_connections
                     WHERE (user_id = %s AND connection_id = %s)
                     OR (user_id = %s AND connection_id = %s)
                     AND status != 'rechazada'"""

            cursor.execute(sql, (user_id, connection_id, connection_id, user_id))

            count = cursor.fetchone()[0]  # lo asigna a la primera columna

            if count == 0:
                # Agregar una nueva solicitud de conexión pendiente
                sql = "INSERT INTO user_connections (user_id, connection_id, status) VALUES (%s, %s, 'pendiente')"
                cursor.execute(sql, (user_id,connection_id))
                db.connection.commit()
                return True
            else:
                # Ya existe una solicitud pendiente o aceptada
                return False
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get_solicitudes(cls, db, user_id):
        try:
            cursor = db.connection.cursor()

            # Obtener todas las solicitudes de conexión pendientes del usuario
            sql = """SELECT user_connections.id, usuario.id_usuario, usuario.a_name, usuario.a_username, usuario.a_ubicacion, usuario.a_imagenperfil
                                 FROM user_connections
                                 JOIN usuario 
                                 ON user_connections.user_id = usuario.id_usuario
                                 WHERE connection_id = %s AND status = 'pendiente'"""
            cursor.execute(sql, (user_id,))
            rows = cursor.fetchall()
            requests = []
            for row in rows:
                requests.append({
                    'id': row[0],
                    'id_usuario': row[1],
                    'name': row[2],
                    'username': row[3],
                    'location': row[4],
                    'profile_image': row[5]
                })
            return requests
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_solicitud_usu(cls, db, requests_list):
        try:
            cursor = db.connection.cursor()

            # Obtener información de los usuarios que mandaron solicitudes
            user_ids = [request['id'] for request in requests_list]
            print()
            if not user_ids:
                return []

            sql = """SELECT uc.id, u.id_usuario, u.a_name, u.a_username, u.a_ubicacion, u.a_imagenperfil
                     FROM user_connections uc
                     INNER JOIN usuario u ON u.id_usuario = uc.user_id
                     WHERE uc.connection_id = %s AND uc.status = 'pendiente'"""
            user_ids_string = ', '.join(str(user_id) for user_id in user_ids)
            cursor.execute(sql, (user_ids_string,))
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append({
                    'id_usuario': row[1],  # Usar el alias "id_usuario"
                    'id_connection': row[0],  # Usar el nombre "id_connection"
                    'name': row[2],
                    'username': row[3],
                    'location': row[4],
                    'profile_image': row[5]
                })
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def aceptar_solicitud(cls, db, request_id):
        try:
            cursor = db.connection.cursor()
            print("jijijaaa")
            # Cambiar el estado de la solicitud de conexión a aceptada
            sql = "UPDATE user_connections SET status = 'aceptada' WHERE id = %s"
            print("jijijaaa")
            cursor.execute(sql, (request_id,))
            print("jijijaaa")
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def rechazar_solicitud(cls, db, request_id):
        try:
            cursor = db.connection.cursor()
            # Eliminar la solicitud de conexión
            sql = "DELETE FROM user_connections WHERE id = %s"
            cursor.execute(sql, (request_id,))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            print("rechazar_soli")
            raise Exception(ex)

    @classmethod
    def get_amigos(cls, db, id_usuario):
        """
        Obtiene los amigos de un usuario dado su id_usuario
        """
        try:
            cursor = db.connection.cursor()
            # Seleccionamos los usuarios amigos de la tabla de amistades
            sql = """SELECT usuario.* FROM usuario 
                    JOIN user_connections 
                    ON (usuario.id_usuario = user_connections.user_id OR usuario.id_usuario = user_connections.connection_id) 
                    WHERE (user_connections.user_id = %s OR user_connections.connection_id = %s) 
                    AND usuario.id_usuario != %s 
                    AND user_connections.status = 'aceptada'"""

            cursor.execute(sql, (id_usuario, id_usuario, id_usuario))
            amigos = cursor.fetchall()

            # Convertimos los resultados en una lista de objetos Usuario
            amigos_list = []
            for amigo in amigos:
                amigo_obj = User(
                    amigo[0],
                    amigo[1],
                    amigo[2],
                    amigo[3],
                    amigo[4],
                    amigo[5],
                    amigo[6],
                    amigo[7],
                    amigo[8]
                )
                amigos_list.append(amigo_obj)

            return amigos_list

        except Exception as ex:
            print("gets_amigos")
            print(str(ex))
            return None

    @classmethod
    def get_no_amigos(cls, db, id_usuario):
        """
        Obtiene los usuarios que no son amigos de un usuario dado su id_usuario
        """
        try:
            cursor = db.connection.cursor()
            # Seleccionamos los usuarios que no están en la tabla de amistades
            sql = """SELECT * FROM usuario 
                    WHERE id_usuario 
                    NOT IN 
                    (SELECT user_id FROM user_connections 
                        WHERE connection_id = %s AND status = 'aceptada' 
                        UNION SELECT connection_id FROM user_connections 
                            WHERE user_id = %s AND status = 'aceptada') 
                        AND id_usuario != %s"""

            cursor.execute(sql, (id_usuario, id_usuario, id_usuario))

            no_amigos = cursor.fetchall()


            # Convertimos los resultados en una lista de objetos Usuario
            no_amigos_list = []

            for no_amigo in no_amigos:
                no_amigo_obj = User(
                    no_amigo[0],
                    no_amigo[1],
                    no_amigo[2],
                    no_amigo[3],
                    no_amigo[4],
                    no_amigo[5],
                    no_amigo[6],
                    no_amigo[7],
                    no_amigo[8]
                )
                no_amigos_list.append(no_amigo_obj)

            return no_amigos_list

        except Exception as ex:
            print(str(ex))
            return []

    @classmethod
    def get_all_users(cls, db):
        try:
            cursor = db.connection.cursor()

            sql = """SELECT id_usuario, a_name, a_username, 
                    a_email, a_descripcion, a_celular, a_ubicacion, a_imagenperfil 
                     FROM usuario """
            cursor.execute(sql)
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append({
                    'id_usuario': row[0],
                    'a_name': row[1],
                    'a_username': row[2],
                    'a_email': row[3],
                    'a_descripcion': row[4],
                    'a_celular': row[5],
                    'a_ubicacion': row[6],
                    'a_imagenperfil': row[7]
                })
            return users
        except Exception as ex:
            raise Exception(ex)