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
        

