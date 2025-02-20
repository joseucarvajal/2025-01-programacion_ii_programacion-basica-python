'''
Tienda: Versión 2.0
Temas:
    - Estructuras de control: if, else

Explicación:
    Se soluciona los problemas de la versión 1.0
        - No se valida que el nombre del producto no sea vacío.
        - No se valida que el costo del producto no sea vacío
        - No se valida que el costo del producto no sea negativo.

Problemas de la versión 2.0:
    - No se puede ingresar más de un producto.
    Cómo solucionar los problemas:
        - Para ingresar más de un producto, se puede utilizar una estructura de repetición: while, for.

'''

nombre_producto = input("Ingrese el nombre del producto: ")
if len(nombre_producto) == 0:
    print("El nombre del producto no puede estar vacío")
else:
    costo_producto = input("Ingrese el costo del producto: ")
    if len(costo_producto) == 0:
        print("El costo del producto no puede estar vacío")
    else:
        costo_producto = float(costo_producto)
        if costo_producto < 0:
            print("El costo del producto no puede ser negativo")
        else:
            print(f"El producto {nombre_producto} tiene un costo de {costo_producto}")
        

