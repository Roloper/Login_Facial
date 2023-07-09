from models.entities.Producto import Prdocuto

class ModelProducto:
    @classmethod
    def create(cls, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO Producto (id_producto, nombre_produc, descripcion, precio_uni, id_usuario) VALUES ({}, '{}', '{}', {}, {})".format(
                producto.id_producto, producto.nombre_produc, producto.descripcion, producto.precio_uni, producto.id_usuario)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def delete(cls, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM Producto WHERE id_producto = {}".format(producto.id_producto)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def update(cls, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE Producto SET nombre_produc = '{}', descripcion = '{}', precio_uni = {}, id_usuario = {} WHERE id_producto = {}".format(
                producto.nombre_produc, producto.descripcion, producto.precio_uni, producto.id_usuario, producto.id_producto)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get(cls, db, id_producto):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM Producto WHERE id_producto = {}".format(id_producto)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                producto = Prdocuto(row[0], row[1], row[2], row[3], row[4])
                return producto
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
