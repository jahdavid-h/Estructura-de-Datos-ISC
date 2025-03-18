import java.util.ArrayList;

class Pila {
    private ArrayList<Integer> pila;
    private int capacidad;

    public Pila(int capacidad) {
        this.capacidad = capacidad;
        this.pila = new ArrayList<>(capacidad);
    }

    public boolean estaVacia() {
        return pila.isEmpty();
    }

    public boolean estaLlena() {
        return pila.size() == capacidad;
    }

    public void push(int elemento) {
        if (estaLlena()) {
            System.out.println("Error: La pila está llena.");
        } else {
            pila.add(elemento);
        }
    }

    public Integer pop() {
        if (estaVacia()) {
            System.out.println("Error: La pila está vacía.");
            return null;
        }
        return pila.remove(pila.size() - 1);
    }

    public Integer peek() {
        if (estaVacia()) {
            System.out.println("Error: La pila está vacía.");
            return null;
        }
        return pila.get(pila.size() - 1);
    }

    public void recorrido() {
        System.out.println(pila);
    }
}

// Ejemplo de uso
public class pilas {
    public static void main(String[] args) {
        Pila pila = new Pila(5);
        pila.push(1);
        pila.push(2);
        pila.push(3);
        pila.recorrido();  // [1, 2, 3]
        System.out.println(pila.pop());  // 3
        System.out.println(pila.peek());  // 2
        System.out.println(pila.estaVacia()); // false
        System.out.println(pila.estaLlena()); // false
    }
}