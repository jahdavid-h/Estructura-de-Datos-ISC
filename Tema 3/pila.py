from collections import deque


class Pilas:
    def __init__(self, max_size=None):
        self.stack = []
        self.max_size = max_size

    def push(self, elemento):
        if self.esta_llena():
            raise Exception("La pila está llena")
        self.stack.append(elemento)

    def pop(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.stack.pop()

    def peek(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.stack[-1]

    def esta_vacia(self):
        return not self.stack

    def esta_llena(self):
        return self.max_size is not None and len(self.stack) >= self.max_size

    def recorrer(self):
        print("Pila:", list(reversed(self.stack)))


class Colas:
    def __init__(self, max_size=None):
        self.queue = deque()
        self.max_size = max_size

    def insertar(self, elemento):
        if self.esta_llena():
            raise Exception("La cola está llena")
        self.queue.append(elemento)

    def eliminar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.queue.popleft()

    def esta_vacia(self):
        return not self.queue

    def esta_llena(self):
        return self.max_size is not None and len(self.queue) >= self.max_size

    def recorrer(self):
        print("Cola:", list(self.queue))


class Main:
    @staticmethod
    def ejecutar():
        pila = Pilas(max_size=3)
        for num in [10, 20, 30]:
            pila.push(num)
        pila.recorrer()
        print("¿Está llena la pila?", pila.esta_llena())
        print("Elemento eliminado:", pila.pop())
        print("Elemento en la cima:", pila.peek())

        cola = Colas(max_size=3)
        for num in [1, 2, 3]:
            cola.insertar(num)
        cola.recorrer()
        print("¿Está llena la cola?", cola.esta_llena())
        print("Elemento eliminado:", cola.eliminar())
        print("Elemento en el frente:", cola.queue[0])


if __name__ == "__main__":
    Main.ejecutar()