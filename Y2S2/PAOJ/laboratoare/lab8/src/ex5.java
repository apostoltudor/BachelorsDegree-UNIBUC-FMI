import java.util.*;

public class ex5 {
    public static void main(String[] args) {
        // 1. Cream HashMap-ul: nume student -> lista de note
        HashMap<String, List<Integer>> catalog = new HashMap<>();

        catalog.put("Ana", Arrays.asList(9, 10, 8));
        catalog.put("Bogdan", Arrays.asList(7, 6, 9));
        catalog.put("Cristina", Arrays.asList(10, 10, 9));
        catalog.put("Dan", Arrays.asList(5, 7, 6));
        catalog.put("Elena", Arrays.asList(9, 8, 10));

        // 2. Calculam si afisam media fiecarui student
        System.out.println("Medii studenti:");
        for (Map.Entry<String, List<Integer>> entry : catalog.entrySet()) {
            String nume = entry.getKey();
            List<Integer> note = entry.getValue();
            double media = note.stream().mapToInt(Integer::intValue).average().orElse(0);
            System.out.println(nume + " -> media: " + media);
        }

        // 3. Afisam studentii cu medii ≥ 8
        System.out.println("\nStudenti cu medii >= 8:");
        for (Map.Entry<String, List<Integer>> entry : catalog.entrySet()) {
            double media = entry.getValue().stream().mapToInt(Integer::intValue).average().orElse(0);
            if (media >= 8) {
                System.out.println(entry.getKey() + " -> media: " + media);
            }
        }

        // 4. Afisam toate perechile nume: nota1, nota2,...
        System.out.println("\nNotele complete:");
        for (Map.Entry<String, List<Integer>> entry : catalog.entrySet()) {
            String nume = entry.getKey();
            List<Integer> note = entry.getValue();
            System.out.println(nume + ": " + note);
        }
    }
}
