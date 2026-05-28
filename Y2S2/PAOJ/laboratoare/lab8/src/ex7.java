import java.util.*;

public class ex7 {
    public static void main(String[] args) {

        // ======= PARTEA 1 – Coada de la ghiseu =======
        Queue<String> coadaGhiseu = new LinkedList<>();

        // Adaugam clienti
        coadaGhiseu.add("Maria");
        coadaGhiseu.add("Ion");
        coadaGhiseu.add("Andreea");
        coadaGhiseu.add("George");

        System.out.println("Coada initiala: " + coadaGhiseu);

        // Procesam clientii (poll scoate primul client)
        while (!coadaGhiseu.isEmpty()) {
            String client = coadaGhiseu.poll();
            System.out.println("Client procesat: " + client);
        }

        // ======= PARTEA 2 – Undo/Redo cu Deque =======
        Deque<String> actiuni = new LinkedList<>();

        // Adaugam actiuni (le punem in fata - ca un stack)
        actiuni.addFirst("Deschide fisier");
        actiuni.addFirst("Scrie text");
        actiuni.addFirst("Sterge linie");
        actiuni.addFirst("Salveaza");

        System.out.println("\nActiuni curente (stiva): " + actiuni);

        // Undo (scoatem ultima actiune facuta)
        String undo = actiuni.removeFirst();
        System.out.println("Undo: " + undo);
        System.out.println("Actiuni dupa undo: " + actiuni);

        // Inca un undo
        undo = actiuni.removeFirst();
        System.out.println("Undo: " + undo);
        System.out.println("Actiuni dupa undo: " + actiuni);
    }
}
