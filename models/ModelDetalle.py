from models.entities.Detalle import Detalle

class ModelDetalle:
    @classmethod
    def create(cls, db, detalle):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO Detalle (id_venta, id_producto, cantidad, precio_total) VALUES ({}, '{}', '{}', {})".format(
                detalle.id_venta, detalle.id_producto, detalle.cantidad, detalle.precio_total)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def delete(cls, db, detalle):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM Detalle WHERE id_venta = {} AND id_producto = {}".format(detalle.id_venta, detalle.id_producto)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def update(cls, db, detalle):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE Detalle SET id_venta = '{}', cantidad = '{}', precio_total = {} WHERE id_venta = {} AND id_producto = {}".format(
                detalle.id_venta, detalle.cantidad, detalle.precio_total, detalle.id_venta, detalle.id_producto)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get(cls, db, id_venta, id_producto):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM Detalle WHERE id_venta = {} AND id_producto = {}".format(id_venta, id_producto)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                detalle = Detalle(row[0], row[1], row[2], row[3])
                return detalle
            else:
                return None
        except Exception as ex:
            raise Exception(ex)



