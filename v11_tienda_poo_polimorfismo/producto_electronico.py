from abc import abstractmethod
from producto import Producto

class ProductoElectronico(Producto):
    _garantia = 0

    def calcular_precio_final(self):
        return self._precio * 1.2

    @property
    def garantia(self):
        return self._garantia

    @garantia.setter
    def garantia(self, nueva_garantia):
        try:
            self._garantia = float(nueva_garantia)
        except ValueError as e:
            raise ValueError(f"La garantia del producto '{self.nombre}' debe ser un valor numérico")

        if(self._precio < 0):
            raise ValueError(f"La garantia del producto '{self.nombre}' no puede ser negativo")


    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia = garantia

