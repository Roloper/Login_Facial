from entities.Venta import Venta

@classmethod
def create_venta(cls, db, venta):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO Venta (fecha, obs, id_usuario)
                    VALUES (%s, %s, %s)"""
            cursor.execute(sql, (venta.fecha, venta.obs, venta.id_usuario))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
        
@classmethod
def get_venta(cls, db, id_venta):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_venta, fecha, obs, id_usuario
                     FROM Venta WHERE id_venta = %s"""
            cursor.execute(sql, (id_venta,))
            row = cursor.fetchone()
            if row is not None:
                venta = Venta(row[0], row[1], row[2], row[3])
                return venta
            else:
                return None
        except Exception as ex:
            raise Exception(ex)   
        
@classmethod
def update_venta(cls, db, venta):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE Venta
                     SET fecha = %s, obs = %s, id_usuario = %s
                     WHERE id_venta = %s"""
            cursor.execute(sql, (venta.fecha, venta.obs, venta.id_usuario, venta.id_venta))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
        
@classmethod
def delete_venta(cls, db, id_venta):
        try:
            cursor = db.connection.cursor()
            sql = """DELETE FROM Venta WHERE id_venta = %s"""
            cursor.execute(sql, (id_venta,))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)