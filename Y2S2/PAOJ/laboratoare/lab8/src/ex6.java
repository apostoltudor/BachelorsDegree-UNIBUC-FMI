import java.util.*;

public class ex6 {
    public static void main(String[] args) {
        // 1. Cream TreeMap-ul (cheile vor fi sortate alfabetic)
        TreeMap<String, Double> produse = new TreeMap<>();

        // 2. Adaugam produse
        produse.put("Paine", 4.5);
        produse.put("Lapte", 6.0);
        produse.put("Oua", 12.0);
        produse.put("Cafea", 30.5);
        produse.put("Zahar", 8.5);
        produse.put("Ulei", 15.0);

        // 3. Afisam lista produselor (TreeMap este sortat alfabetic automat)
        System.out.println("Lista produselor (sortate alfabetic):");
        for (Map.Entry<String, Double> entry : produse.entrySet()) {
            System.out.println(entry.getKey() + " - " + entry.getValue() + " lei");
        }

        // 4. Calculam pretul total
        double total = 0;
        for (double pret : produse.values()) {
            total += pret;
        }
        System.out.println("\nPret total: " + total + " lei");

        // 5. Cautam produsul cu pretul cel mai mare
        String produsMax = "";
        double pretMax = Double.MIN_VALUE;
        for (Map.Entry<String, Double> entry : produse.entrySet()) {
            if (entry.getValue() > pretMax) {
                pretMax = entry.getValue();
                produsMax = entry.getKey();
            }
        }

        System.out.println("\nProdusul cel mai scump: " + produsMax + " - " + pretMax + " lei");
    }
}
