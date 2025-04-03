from abc import abstractmethod
from producto import Producto

class ProductoAlimenticio(Producto):
    _fecha_caducidad = ""

    def calcular_precio_final(self):
        return self._precio * 0.9

    @property
    def fecha_caducidad(self):
        return self._fecha_caducidad

    @fecha_caducidad.setter
    def fecha_caducidad(self, nueva_fecha_caducidad):
        self._fecha_caducidad = nueva_fecha_caducidad

    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad
