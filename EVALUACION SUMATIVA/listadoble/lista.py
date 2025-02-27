class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0
    
    def esta_vacia(self):
        return self.tamano == 0
    
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.final
            self.final = nuevo_nodo
        self.tamano += 1
    
    def eliminar(self):
        if self.esta_vacia():
            print("La cola esta vacia. No se puede eliminar.")
            return None
        valor = self.frente.valor
        if self.frente == self.final:
            self.frente = self.final = None
        else:
            self.frente = self.frente.siguiente
            self.frente.anterior = None
        self.tamano -= 1
        return valor
    
    def ver_frente(self):
        if self.esta_vacia():
            print("La cola esta vacia.")
            return None
        return self.frente.valor
    
    def ver_final(self):
        if self.esta_vacia():
            print("La cola esta vacia.")
            return None
        return self.final.valor
    
    def mostrar(self):
        if self.esta_vacia():
            print("La cola esta vacia.")
            return
        actual = self.frente
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
        print("FIN")

# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola()
    cola.agregar(10)
    cola.agregar(20)
    cola.agregar(30)
    
    print("Contenido de la cola:")
    cola.mostrar()
    
    print("\nEliminando un elemento:", cola.eliminar())
    
    print("\nContenido de la cola despues de eliminar:")
    cola.mostrar()
    
    print("\nEl primer elemento en la cola es:", cola.ver_frente())
    print("El ultimo elemento en la cola es:", cola.ver_final())
