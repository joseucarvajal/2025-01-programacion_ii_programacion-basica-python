'''
Tienda: Versión 1.0
Temas:
    - Variables
    - Input
    - Output

Explicación:
    Se solicita el nombre del producto y el costo del producto.
    Se muestra el nombre del producto y el costo del producto.

Problemas de la versión 1.0:
    - No se valida que el nombre del producto no sea vacío.
    - No se valida que el costo del producto no sea vacío
    - No se valida que el costo del producto no sea negativo.

    Cómo solucionar los problemas:
        - Utilizar estructuras de control para validar los datos de entrada: if, else.
'''

nombre_producto = input("Ingrese el nombre del producto: ")
costo_producto = input("Ingrese el costo del producto: ")

print(f"El producto {nombre_producto} tiene un costo de {costo_producto}")