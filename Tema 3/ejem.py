from collections import deque


class Pilas:
    def __init__(self):
        self.stack = []

    def push(self, elemento):
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

    def recorrer(self):
        print("Pila:", list(reversed(self.stack)))


class Colas:
    def __init__(self):
        self.queue = deque()

    def insertar(self, elemento):
        self.queue.append(elemento)

    def eliminar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.queue.popleft()

    def esta_vacia(self):
        return not self.queue

    def recorrer(self):
        print("Cola:", list(self.queue))


class Main:
    @staticmethod
    def ejecutar():
        pila = Pilas()
        for num in [10, 20, 30]:
            pila.push(num)
        pila.recorrer()
        print("Elemento eliminado:", pila.pop())
        print("Elemento en la cima:", pila.peek())

        cola = Colas()
        for num in [1, 2, 3]:
            cola.insertar(num)
        cola.recorrer()
        print("Elemento eliminado:", cola.eliminar())
        print("Elemento en el frente:", cola.queue[0])


if __name__ == "__main__":
    Main.ejecutar()