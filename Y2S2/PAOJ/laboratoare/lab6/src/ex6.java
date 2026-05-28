import java.util.*;

public class ex6 {

    // Metodă generică cu wildcard
    public static void printList(List<? extends Number> lista) {
        for (Number num : lista) {
            System.out.println(num);
        }
    }

    public static void main(String[] args) {
        // Listă de Integer
        List<Integer> listaInt = Arrays.asList(1, 2, 3, 4, 5);
        System.out.println("Lista de Integer:");
        printList(listaInt);

        // Listă de Double
        List<Double> listaDouble = Arrays.asList(1.5, 2.3, 3.7);
        System.out.println("Lista de Double:");
        printList(listaDouble);

        // Listă de Float
        List<Float> listaFloat = Arrays.asList(2.1f, 3.2f);
        System.out.println("Lista de Float:");
        printList(listaFloat);
    }
}
