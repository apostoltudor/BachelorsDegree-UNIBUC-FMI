import java.util.*;

public class ex5 {

    // 1. Clasa Persoana
    public static class Persoana {
        private String nume;
        private int varsta;

        public Persoana(String nume, int varsta) {
            this.nume = nume;
            this.varsta = varsta;
        }

        public String getNume() {
            return nume;
        }

        public int getVarsta() {
            return varsta;
        }

        @Override
        public String toString() {
            return nume + " (" + varsta + " ani)";
        }
    }

    public static void main(String[] args) {
        // 2. Listă de persoane
        List<Persoana> persoane = new ArrayList<>();
        persoane.add(new Persoana("Andrei", 25));
        persoane.add(new Persoana("Maria", 22));
        persoane.add(new Persoana("Ion", 30));
        persoane.add(new Persoana("Elena", 21));

        // 3a. Sortare după vârstă cu lambda
        persoane.sort((p1, p2) -> Integer.compare(p1.getVarsta(), p2.getVarsta()));

        System.out.println("Sortat după vârstă:");
        persoane.forEach(System.out::println);

        // 3b. Sortare după nume cu Comparator.comparing și method reference
        persoane.sort(Comparator.comparing(Persoana::getNume));

        System.out.println("\nSortat după nume:");
        persoane.forEach(System.out::println);
    }
}
