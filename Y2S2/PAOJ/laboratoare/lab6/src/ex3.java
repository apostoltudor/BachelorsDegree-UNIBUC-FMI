public class ex3 {

    // 1. Clasa Departament
    public static class Departament {
        private String nume;
        private int cod;

        public Departament(String nume, int cod) {
            this.nume = nume;
            this.cod = cod;
        }

        public Departament(Departament other) {
            this.nume = other.nume;
            this.cod = other.cod;
        }

        public void setNume(String nume) {
            this.nume = nume;
        }

        public String getNume() {
            return nume;
        }

        public int getCod() {
            return cod;
        }
    }

    // 2. Clasa Angajat
    public static class Angajat implements Cloneable {
        private String nume;
        private Departament departament;

        public Angajat(String nume, Departament departament) {
            this.nume = nume;
            this.departament = departament;
        }

        // Shallow copy
        public Angajat shallowCopy() throws CloneNotSupportedException {
            return (Angajat) this.clone();
        }

        // Deep copy
        public Angajat deepCopy() {
            Departament deptCopy = new Departament(departament); // deep copy la obiectul intern
            return new Angajat(this.nume, deptCopy);
        }

        public void setDepartamentName(String nouNume) {
            this.departament.setNume(nouNume);
        }

        public void printInfo() {
            System.out.println("Angajat: " + nume + ", Departament: " + departament.getNume());
        }
    }

    public static void main(String[] args) throws CloneNotSupportedException {
        Departament d1 = new Departament("IT", 101);
        Angajat a1 = new Angajat("Andrei", d1);

        Angajat shallow = a1.shallowCopy();
        Angajat deep = a1.deepCopy();

        // modific departamentul în copie
        shallow.setDepartamentName("HR");
        deep.setDepartamentName("Financiar");

        System.out.println("Original:");
        a1.printInfo();            // afectat de shallow
        System.out.println("Shallow Copy:");
        shallow.printInfo();       // HR
        System.out.println("Deep Copy:");
        deep.printInfo();          // Financiar
    }
}
