'''
Tienda: Versión 5.0
Temas:
    - Manejo o gestión de errores: try, except

Explicación:
    Se soluciona los problemas de la versión 4.0
        - Hay errores no controlados o no gestionados. Ejemplo:
            - Si un usuario ingresa una letra en lugar de un número en el costo del producto.


Problemas de la versión 5.0:
    - Se repite el código para validar el costo del producto y si quisiéramos agregar otras variables,
    por ejemplo: descuento, habría que repetir el mismo código de "costo del producto"

    Cómo solucionar los problemas:
        - Para evitar repetir código, se puede utilizar una función o rutina para validar cualquier variable float positiva.
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
                try:
                    costo_producto = float(costo_producto)
                except ValueError:
                    print(f"El costo del producto {i+1} no es un número válido")
                    continue

                if costo_producto < 0:
                    print(f"El costo del producto {i+1} no puede ser negativo")
                else:
                    print(f"El producto {nombre_producto} tiene un costo de {costo_producto}")
                    total_costo += costo_producto
                    print(f"Hasta ahora ha registrado {i+1} productos")
                    print(f"El total parcial de la compra es {total_costo}")
                    i += 1
print(f"El total de la compra es {total_costo}")
print("Gracias por su compra")