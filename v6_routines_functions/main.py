'''
Tienda: Versión 6.0
Temas:
    - Evitar repetir código, mediante el uso de funciones o rutinas
    - Usar funciones o rutinas

Explicación:
    Se soluciona los problemas de la versión 5.0
        - Se repite el código para validar el costo del producto y si quisiéramos agregar otras variables,
        por ejemplo: descuento, habría que repetir el mismo código de "costo del producto"


Problemas de la versión 6.0:
    - El código tiene dificultades para crecer, es decir, si quisiéramos agregar más funcionalidades a la tienda, 
    como promociones, manejo de impuestos, etc., el código se volvería cada vez más grande y difícil de mantener.
    - NO hay encapsulamiento de valores importantes como valor del producto, descuento, etc. Haciendo que estos valores
    se puedan modificar desde cualquier parte del código de manera insegura.
    - No hay una separación entre el código de entrada de datos y el código de procesamiento de datos.
    - No hay una separación de responsabilidades claras en esta versión del código
    Solución:
        - Programación Orientada a Objetos (POO)
      
'''

def solicitar_y_validar_valor_float_positivo(nombre_variable):
    valor_de_la_variable = input(f"Ingrese {nombre_variable}: ")
    if len(valor_de_la_variable) == 0:
        print(f"{nombre_variable} no puede estar vacío")
        raise ValueError(f"{nombre_variable} no puede estar vacío")
    else:
        try:
            valor_de_la_variable = float(valor_de_la_variable)
        except ValueError:
            print(f"{nombre_variable} no es un número válido")
            raise ValueError(f"{nombre_variable} no es un número válido")
        if valor_de_la_variable < 0:
            print(f"{nombre_variable} no puede ser negativo")
            raise ValueError(f"{nombre_variable} no puede ser negativo")
        else:
            return valor_de_la_variable



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
            try:
                costo_producto = solicitar_y_validar_valor_float_positivo(f"costo del producto {i+1}: ")
                descuento = solicitar_y_validar_valor_float_positivo(f"descuento del producto {i+1}: ")
            except ValueError as e:
                continue
            
            costo_producto = costo_producto - descuento

            total_costo += costo_producto
            print(f"Hasta ahora ha registrado {i+1} productos")
            print(f"El total parcial de la compra es {total_costo}")
            i += 1
print(f"El total de la compra es {total_costo}")
print("Gracias por su compra")



