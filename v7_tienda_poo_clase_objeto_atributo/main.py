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

class Tienda:
    nombre = ""

producto1 = Producto()
producto1.precio = 100.0

producto2 = Producto()
producto2.nombre = "Producto 2"
producto2.precio = 200.0

producto3 = Producto()
producto3.nombre = "Producto 3"
producto3.precio = 300.0

producto4 = Producto()
producto4.nombre = "Producto 4"
producto4.precio = 400.0

total_costo = producto1.precio + producto2.precio + producto3.precio + producto4.precio
print(f"El total de la compra es {total_costo}")

