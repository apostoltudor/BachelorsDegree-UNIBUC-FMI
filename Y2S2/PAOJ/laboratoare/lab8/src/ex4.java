import java.util.*;

public class ex4 {

    public static class Produs implements Comparable<Produs> {
        private String nume;
        private double pret;

        public Produs(String nume, double pret) {
            this.nume = nume;
            this.pret = pret;
        }

        public String getNume() {
            return nume;
        }

        public double getPret() {
            return pret;
        }

        @Override
        public int compareTo(Produs altProdus) {
            return Double.compare(this.pret, altProdus.pret); // sortare crescătoare după preț
        }

        @Override
        public String toString() {
            return nume + " - " + pret + " lei";
        }
    }

    public static void main(String[] args) {
        // 1. TreeSet cu sortare naturală (după preț)
        TreeSet<Produs> produseDupaPret = new TreeSet<>();
        produseDupaPret.add(new Produs("Paine", 3.5));
        produseDupaPret.add(new Produs("Lapte", 6.2));
        produseDupaPret.add(new Produs("Cafea", 18.0));
        produseDupaPret.add(new Produs("Zahar", 5.0));
        produseDupaPret.add(new Produs("Orez", 4.5));

        System.out.println("Produse sortate crescător după preț:");
        for (Produs p : produseDupaPret) {
            System.out.println(p);
        }

        // 2. TreeSet cu sortare descrescătoare după nume
        Comparator<Produs> comparatorDupaNumeDesc = (p1, p2) -> p2.getNume().compareTo(p1.getNume());
        TreeSet<Produs> produseDupaNumeDesc = new TreeSet<>(comparatorDupaNumeDesc);
        produseDupaNumeDesc.addAll(produseDupaPret); // refolosim produsele deja create

        System.out.println("\nProduse sortate descrescător după nume:");
        for (Produs p : produseDupaNumeDesc) {
            System.out.println(p);
        }
    }
}
