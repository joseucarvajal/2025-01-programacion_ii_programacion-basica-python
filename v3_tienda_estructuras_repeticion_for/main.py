'''
Tienda: Versión 3.0
Temas:
    - Estructuras de repetición: for

Explicación:
    Se soluciona los problemas de la versión 2.0
        - No se puede ingresar más de un producto.

Problemas de la versión 3.0:
    - Usualmente, se desconoce la cantidad de productos que se van a procesar.

Cómo solucionar los problemas:
    - Utilizar una estructura de repetición donde no se conoce la cantidad de veces que se va a repetir el bloque de código.
    en este caso, se utiliza la estructura de repetición while
'''

cuantos_productos = input("Ingrese la cantidad de productos: ")
total_costo = 0
if len(cuantos_productos) == 0:
    print("La cantidad de productos no puede estar vacía")
else:
    cuantos_productos = int(cuantos_productos)
    if(cuantos_productos <= 0):
        print("Debe llevar minimo 1 producto")
    else:
        print(f"Se procesarán {cuantos_productos} productos")
        for i in range(cuantos_productos):
            nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
            if len(nombre_producto) == 0:
                print(f"El nombre del producto {i+1} no puede estar vacío")
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

        print(f"El total de la compra es {total_costo}")
        print("Gracias por su compra")