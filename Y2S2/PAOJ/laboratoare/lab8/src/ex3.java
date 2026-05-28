import java.util.*;

public class ex3 {
    public static void main(String[] args) {
        // 1. Definirea colecțiilor
        HashSet<String> oraseHash = new HashSet<>();
        TreeSet<String> oraseTree = new TreeSet<>();

        // 2. Adăugăm orașe (inclusiv duplicate)
        List<String> listaOrase = Arrays.asList(
                "Bucuresti", "Cluj", "Iasi", "Timisoara", "Constanta",
                "Brasov", "Oradea", "Sibiu", "Arad", "Cluj"  // Cluj e duplicat
        );

        // Le adăugăm în ambele seturi
        oraseHash.addAll(listaOrase);
        oraseTree.addAll(listaOrase);

        // 3. Comparăm mărimile și conținutul
        System.out.println("HashSet conține " + oraseHash.size() + " orașe: " + oraseHash);
        System.out.println("TreeSet conține " + oraseTree.size() + " orașe: " + oraseTree);

        // 4. Afișăm ordonat orașele din TreeSet
        System.out.println("\nOrașele în ordine alfabetică:");
        for (String oras : oraseTree) {
            System.out.println(oras);
        }

        // 5. Verificăm dacă un oraș introdus de utilizator există în HashSet
        Scanner scanner = new Scanner(System.in);
        System.out.print("\nIntrodu un oraș de verificat: ");
        String cautat = scanner.nextLine();

        if (oraseHash.contains(cautat)) {
            System.out.println("Orașul \"" + cautat + "\" se află în listă.");
        } else {
            System.out.println("Orașul \"" + cautat + "\" NU se află în listă.");
        }
    }
}
