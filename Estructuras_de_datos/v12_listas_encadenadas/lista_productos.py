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
    

    def buscar_producto_segun_nombre(self, nombre_a_buscar):
        nodo_tmp = self._head
        while nodo_tmp is not None:
            if nodo_tmp.producto.nombre == nombre_a_buscar:
                return nodo_tmp.producto
            nodo_tmp = nodo_tmp.siguiente

        return None
    
    def eliminar_producto_segun_nombre(self, nombre_a_eliminar):
        if self._head.producto.nombre == nombre_a_eliminar:
            self._head = self._head.siguiente
        else:
            nodo_tmp = self._head
            while nodo_tmp.siguiente is not None:
                if nodo_tmp.siguiente.producto.nombre == nombre_a_eliminar:
                    nodo_tmp.siguiente = nodo_tmp.siguiente.siguiente
                else:
                    nodo_tmp = nodo_tmp.siguiente