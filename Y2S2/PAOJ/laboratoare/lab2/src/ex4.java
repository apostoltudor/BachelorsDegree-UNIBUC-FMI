public class ex4 {
    public static class Persoana {
        private String nume;
        private int varsta;
        private double[] venit;
        private static int nrPersoane;
        private int id;

        // bloc static – o singură dată la încărcarea clasei
        static {
            nrPersoane = 0;
        }

        // bloc nestatic – de fiecare dată când se creează un obiect
        {
            this.id = ++nrPersoane;
        }

        // Constructor implicit
        public Persoana() {
            this.nume = "Necunoscut";
            this.varsta = 0;
            this.venit = new double[12];
        }

        // Constructor parametrizat
        public Persoana(String nume, int varsta, double[] venit) {
            this.nume = nume;
            this.varsta = varsta;
            this.venit = venit;
        }

        // Constructor de copiere (deep copy)
        public Persoana(Persoana other) {
            this.nume = other.nume;
            this.varsta = other.varsta;
            this.venit = new double[12];
            for (int i = 0; i < 12; i++) {
                this.venit[i] = other.venit[i];
            }
        }

        // Getteri și setteri
        public String getNume() {
            return nume;
        }

        public void setNume(String nume) {
            this.nume = nume;
        }

        public int getVarsta() {
            return varsta;
        }

        public void setVarsta(int varsta) {
            this.varsta = varsta;
        }

        public double[] getVenit() {
            return venit;
        }

        public void setVenit(double[] venit) {
            this.venit = venit;
        }

        public int getId() {
            return id;
        }

        public static int getNrPersoane() {
            return nrPersoane;
        }
    }

    public static void main(String[] args) {
        Persoana x = new Persoana();
        System.out.println("Nume implicit: " + x.getNume());

        x.setNume("Ion");
        System.out.println("Nume modificat: " + x.getNume());

        System.out.println("ID persoană: " + x.getId());
        System.out.println("Total persoane create: " + Persoana.getNrPersoane());
    }
}
