from abc import abstractmethod

class Producto:
    _nombre = ""
    _precio = 0.0

    @abstractmethod
    def calcular_precio_final(self):
        pass

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if(len(nuevo_nombre) == 0):
            raise ValueError("El nombre del producto no puede estar vacío")
        self._nombre = nuevo_nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        try:
            self._precio = float(nuevo_precio)
        except ValueError as e:
            raise ValueError(f"El precio del producto '{self.nombre}' debe ser un valor numérico")

        if(self._precio < 0):
            raise ValueError(f"El precio del producto '{self.nombre}' no puede ser negativo")


    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

