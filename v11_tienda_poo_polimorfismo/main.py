'''
Tienda: Versión 9.0 - Programación Orientada a Objetos (POO)
Temas:
    - Herencia
Explicación:
    En esta versión, pasamos a usar POO para solucionar los problemas de la versión 6.0.

'''

from producto_electronico import ProductoElectronico
from producto_alimenticio import ProductoAlimenticio

try:
    print("Tienda: Versión 9.0")

    producto1 = ProductoElectronico("Producto electronico 1", 500.0, 12)
    producto2 = ProductoAlimenticio("Producto alimenticio 1", 200.0, "2025-01-01")

    productos = [producto1, producto2]

    total_costo = 0
    for producto in productos:
        total_costo += producto.calcular_precio_final()
    
    print(f"El total de la compra es {total_costo}")


except ValueError as e:
    print(e)


