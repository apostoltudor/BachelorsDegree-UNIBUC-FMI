import java.util.*;

public class ex2 {
    public static void main(String[] args) {
        LinkedList<String> taskuri = new LinkedList<>();

        // Adăugăm taskuri la început și sfârșit
        taskuri.addFirst("Trimite raportul");       // început
        taskuri.addLast("Verifică emailurile");     // sfârșit
        taskuri.addLast("Scrie documentația");
        taskuri.addFirst("Repornește serverul");

        System.out.println("Taskuri inițiale:");
        for (String task : taskuri) {
            System.out.println(task);
        }

        // Marcăm un task ca finalizat (îl ștergem)
        System.out.println("\nFinalizăm primul task...");
        taskuri.removeFirst(); // sau taskuri.remove("Repornește serverul");

        // Afișăm taskurile în ordine inversă
        System.out.println("\nTaskuri în ordine inversă:");
        Iterator<String> it = taskuri.descendingIterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }

        // Mutăm taskurile cu "urgent" la începutul listei
        taskuri.add("urgent: actualizează baza de date");
        taskuri.add("urgent: trimite backup");
        taskuri.add("curăță biroul");

        System.out.println("\nTaskuri înainte de reorganizare:");
        for (String task : taskuri) {
            System.out.println(task);
        }

        mutaUrgenteInFata(taskuri);

        System.out.println("\nTaskuri după mutarea celor urgente în față:");
        for (String task : taskuri) {
            System.out.println(task);
        }
    }

    public static void mutaUrgenteInFata(LinkedList<String> lista) {
        List<String> urgente = new ArrayList<>();
        Iterator<String> it = lista.iterator();

        while (it.hasNext()) {
            String t = it.next();
            if (t.toLowerCase().contains("urgent")) {
                urgente.add(t);
                it.remove();
            }
        }

        Collections.reverse(urgente); // ca să păstrăm ordinea invers când le adăugăm în față
        for (String t : urgente) {
            lista.addFirst(t);
        }
    }
}
