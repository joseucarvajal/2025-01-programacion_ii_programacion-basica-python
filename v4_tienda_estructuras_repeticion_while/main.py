'''
Tienda: Versión 4.0
Temas:
    - Estructuras de repetición: while

Explicación:
    Se soluciona los problemas de la versión 3.0
        - Usualmente, se desconoce la cantidad de productos que se van a procesar.

Problemas de la versión 4.0:
    - Hay errores no controlados o no gestionados. Ejemplo:
        - Si un usuario ingresa una letra en lugar de un número en el costo del producto.

Cómo solucionar los problemas:
    - Utilizar instrucciones para gestionar los errores no controlados: try, except
'''

i=0
total_costo = 0
continuar = True
while continuar:
    nombre_producto = input(f"Ingrese el nombre del producto {i+1} o (x) para terminar: ")
    if len(nombre_producto) == 0:
        print(f"El nombre del producto {i+1} no puede estar vacío")
    else:
        if nombre_producto == "x":
            continuar = False
        else:
            costo_producto = input(f"Ingrese el costo del producto {i+1}: ")
            if len(costo_producto) == 0:
                print(f"El costo del producto {i+1} no puede estar vacío")
            else:
                costo_producto = float(costo_producto)
                if costo_producto < 0:
                    print(f"El costo del producto {i+1} no puede ser negativo")
                else:
                    print(f"El producto {nombre_producto} tiene un costo de {costo_producto}")
                    total_costo += costo_producto
                    print(f"El total parcial de la compra es {total_costo}")
                    i += 1
print(f"El total de la compra es {total_costo}")
print("Gracias por su compra")