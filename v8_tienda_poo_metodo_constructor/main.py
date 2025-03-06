'''
Tienda: Versión 7.0 - Programación Orientada a Objetos (POO)
Temas:
    - Clases, objetos, atributos

Explicación:
    En esta versión, pasamos a usar POO para solucionar los problemas de la versión 6.0.

Problemas de la versión 7.0:
    - Se pueden crear productos sin nombre
        Solución:
            - Validar que el nombre del producto no esté vacío en el metodo constructor de la clase Producto

'''

class Producto:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        if(len(nombre) == 0):
            raise ValueError("El nombre del producto no puede estar vacío")
        
        self.precio = precio



class Tienda:
    nombre = ""

producto1 = Producto("Producto 1", 100.0)


producto2 = Producto("Producto 2", 200.0)

producto3 = Producto("Producto 3", 300.0)

producto4 = Producto("Producto 4", 400.0)

total_costo = producto1.precio + producto2.precio + producto3.precio + producto4.precio
print(f"El total de la compra es {total_costo}")

