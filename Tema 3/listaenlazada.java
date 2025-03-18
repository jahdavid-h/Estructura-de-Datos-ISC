class Nodo {
    int dato;
    Nodo siguiente;

    public Nodo(int dato) {
        this.dato = dato;
        this.siguiente = null;
    }
}

class ListaEnlazadaOrdenada {
    private Nodo cabeza;

    public ListaEnlazadaOrdenada() {
        this.cabeza = null;
    }

    public void insertar(int dato) {
        Nodo nuevoNodo = new Nodo(dato);

        if (cabeza == null || dato < cabeza.dato) {
            nuevoNodo.siguiente = cabeza;
            cabeza = nuevoNodo;
            return;
        }

        Nodo actual = cabeza;
        while (actual.siguiente != null && actual.siguiente.dato < dato) {
            actual = actual.siguiente;
        }

        nuevoNodo.siguiente = actual.siguiente;
        actual.siguiente = nuevoNodo;
    }

    public void borrar(int dato) {
        if (cabeza == null) {
            System.out.println("La lista está vacía");
            return;
        }

        if (cabeza.dato == dato) {
            cabeza = cabeza.siguiente;
            return;
        }

        Nodo actual = cabeza;
        while (actual.siguiente != null && actual.siguiente.dato != dato) {
            actual = actual.siguiente;
        }

        if (actual.siguiente != null) {
            actual.siguiente = actual.siguiente.siguiente;
        } else {
            System.out.println("Elemento no encontrado");
        }
    }

    public void recorrer() {
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.print(actual.dato + " -> ");
            actual = actual.siguiente;
        }
        System.out.println("None");
    }

    public boolean buscar(int dato) {
        Nodo actual = cabeza;
        while (actual != null) {
            if (actual.dato == dato) {
                return true;
            }
            actual = actual.siguiente;
        }
        return false;
    }

    public boolean estaVacia() {
        return cabeza == null;
    }
}

public class listaenlazada {
    public static void main(String[] args) {
        ListaEnlazadaOrdenada lista = new ListaEnlazadaOrdenada();

        lista.insertar(10);
        lista.insertar(5);
        lista.insertar(20);
        lista.insertar(15);
        System.out.println("Lista después de insertar elementos:");
        lista.recorrer();

        System.out.println("¿Está el 10 en la lista? " + lista.buscar(30));
        System.out.println("¿Está el 7 en la lista? " + lista.buscar(7));

        lista.borrar(10);
        System.out.println("Lista después de borrar 10:");
        lista.recorrer();

        System.out.println("¿Está vacía la lista? " + lista.estaVacia());
    }
}
