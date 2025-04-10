from lista_productos import ListaProductos
from producto import Producto
# Por efectos de tiempo en clase, se omite la gestion de errores. 
# Sin embargo, ustedes deben realizar dicha gestion de errores en sus proyectos/trabajos.


lista_productos = ListaProductos()

while True:
    print("Ingrese una opcion:")
    print("1. Agregar producto")
    print("2. Mostrar total de la compra")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(nombre, precio)
        lista_productos.agregar_producto(producto)

    elif opcion == 2:
        total = lista_productos.obtener_total_compra()
        print(f"El total de la compra es: {total}")

    elif opcion == 3:
        break
    