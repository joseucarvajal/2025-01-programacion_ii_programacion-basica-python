'''
Tienda: Versión 9.0 - Programación Orientada a Objetos (POO)
Temas:
    - Encapsulamiento

Explicación:
    En esta versión, pasamos a usar POO para solucionar los problemas de la versión 6.0.

Problemas de la versión 8.0:
    - Se pueden asignar valores negativos al precio del producto luego de haber sido creado el objeto
        Solución:
            - Encapsular el atributo precio para que no pueda ser accedido directamente
'''

class Producto:
    _nombre = ""
    _precio = 0.0

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

class Tienda:
    nombre = ""

try:
    print("Tienda: Versión 9.0")
    producto1 = Producto("Producto 1", 100.0)

    producto2 = Producto("Producto 2", 600.0)

    producto3 = Producto("Producto 3", 300.0)

    producto4 = Producto("Producto 4", 400.0)

    total_costo = producto1._precio + producto2._precio + producto3._precio + producto4._precio
    print(f"El total de la compra es {total_costo}")

except ValueError as e:
    print(e)


