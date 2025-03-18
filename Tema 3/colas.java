import java.util.LinkedList;

class Cola {
    private LinkedList<Integer> cola;
    private int capacidad;

    public Cola(int capacidad) {
        this.capacidad = capacidad;
        this.cola = new LinkedList<>();
    }

    public boolean estaVacia() {
        return cola.isEmpty();
    }

    public boolean estaLlena() {
        return cola.size() == capacidad;
    }

    public void insertar(int elemento) {
        if (estaLlena()) {
            System.out.println("Error: La cola está llena.");
        } else {
            cola.addLast(elemento);
        }
    }

    public Integer eliminar() {
        if (estaVacia()) {
            System.out.println("Error: La cola está vacía.");
            return null;
        }
        return cola.removeFirst();
    }

    public void recorrido() {
        System.out.println(cola);
    }
}

// Ejemplo de uso
public class colas {
    public static void main(String[] args) {
        Cola cola = new Cola(5);
        cola.insertar(1);
        cola.insertar(2);
        cola.insertar(3);
        cola.recorrido();  // [1, 2, 3]
        System.out.println(cola.eliminar());  // 1
        cola.recorrido();  // [2, 3]
        System.out.println(cola.estaVacia());  // false
        System.out.println(cola.estaLlena());  // false
    }
}