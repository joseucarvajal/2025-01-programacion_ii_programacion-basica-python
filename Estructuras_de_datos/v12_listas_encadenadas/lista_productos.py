from nodo_producto import NodoProducto

class ListaProductos:
    _head = None

    def agregar_producto(self, nuevo_producto):
        nuevo_nodo = NodoProducto(nuevo_producto)

        if self._head is None:
            self._head = nuevo_nodo

        else:
            ultimo_nodo = self._head

            while ultimo_nodo.siguiente is not None:
                ultimo_nodo = ultimo_nodo.siguiente

            ultimo_nodo.siguiente = nuevo_nodo
            
    def obtener_total_compra(self):
        total = 0
        nodo_actual = self._head

        while nodo_actual is not None:
            total += nodo_actual.producto.precio
            nodo_actual = nodo_actual.siguiente

        return total
            