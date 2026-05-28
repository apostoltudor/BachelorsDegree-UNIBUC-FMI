public class ex4 {

    // 1. Clasa Carte care implementează Cloneable
    public static class Carte implements Cloneable {
        private String titlu;
        private String autor;

        public Carte(String titlu, String autor) {
            this.titlu = titlu;
            this.autor = autor;
        }

        public String getTitlu() {
            return titlu;
        }

        public String getAutor() {
            return autor;
        }

        // 2. Suprascriem metoda clone()
        @Override
        public Object clone() {
            try {
                return super.clone(); // shallow copy (suficient aici deoarece avem doar tipuri primitive și String)
            } catch (CloneNotSupportedException e) {
                return null;
            }
        }

        @Override
        public String toString() {
            return "Carte{" + "titlu='" + titlu + '\'' + ", autor='" + autor + '\'' + '}';
        }
    }

    // 3. Metodă statică care clonează dacă obiectul este Cloneable
    public static Object cloneIfPossible(Object obj) {
        if (obj instanceof Cloneable && obj instanceof Carte) {
            return ((Carte) obj).clone(); // forțăm conversia și apelăm metoda clone
        }
        return null;
    }

    public static void main(String[] args) {
        // Cream o carte
        Carte original = new Carte("Ion", "Liviu Rebreanu");

        // Încercăm să o clonăm
        Carte copie = (Carte) cloneIfPossible(original);

        // Afișăm rezultatele
        System.out.println("Original: " + original);
        System.out.println("Copie:    " + copie);
    }
}
