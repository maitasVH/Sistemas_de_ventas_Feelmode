from modelos.Db import Db

class Productos(Db.Model):
    _tablename_='productos'

    id = Db.column(Db.integer, primary_key=True)
    Nombre_producto = Db.Column(Db.String(50), unique=True, nullable=False)
    precio = Db.Column(Db.Float, nullable=False)
    stock = Db.Column(Db.Integer, nullable=False)

    def _init_(self, Nombre_producto, precio, stock):
        self.Nombre_producto = nombre_del_producto
        self.precio = precio
        self.stock = stock

    def serializar(self):
        devolucion{
            'id': self.id,
            'Nombre_del_producto': self.Nombre_producto,
            'precio': self.precio,
            'stock': self.stock
        }
