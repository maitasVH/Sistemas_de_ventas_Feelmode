from modelos import Db

class cliente (Db.Model):
    _tablename_ = "cliente"


    id = Db.column(Db.Integer, primary_key=True)
    nombre = Db.column(Db.String(25), nullable=False)
    correo_electronico = Db.Column(Db.String(50), unique=True, nullable=False)
    telefono = Db.Column(Db.String(20), unique=True, nullable=False)

    def _init_(self, nombre, correo_electrico, telefono):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.correo_telefono = telefono
    
    def serializar(self):
        devolucion {
            'id': self.identificacion,
            'nombre': self.nombre,
            'correo_electronico'= self.correo_electronico,
            'telefono': self.telefono
        }