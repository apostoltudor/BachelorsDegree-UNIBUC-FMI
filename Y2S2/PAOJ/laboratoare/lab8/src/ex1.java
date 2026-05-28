import java.util.*;

public class ex1 {

    public static class Student {
        private String nume;
        private int grupa;
        private double medie;

        public Student(String nume, int grupa, double medie) {
            this.nume = nume;
            this.grupa = grupa;
            this.medie = medie;
        }

        public String getNume() {
            return nume;
        }

        public int getGrupa() {
            return grupa;
        }

        public double getMedie() {
            return medie;
        }

        @Override
        public String toString() {
            return nume + " - Grupa: " + grupa + ", Medie: " + medie;
        }
    }

    public static void main(String[] args) {
        ArrayList<Student> studenti = new ArrayList<>();

        // Adăugăm 6 studenți
        studenti.add(new Student("Ana", 231, 9.3));
        studenti.add(new Student("Bogdan", 232, 7.5));
        studenti.add(new Student("Cristina", 231, 8.1));
        studenti.add(new Student("Dan", 233, 9.3));
        studenti.add(new Student("Elena", 232, 6.8));
        studenti.add(new Student("Florin", 233, 7.9));

        // Sortare descrescătoare după medie
        studenti.sort((s1, s2) -> Double.compare(s2.getMedie(), s1.getMedie()));

        System.out.println("Studenți sortați descrescător după medie:");
        for (Student s : studenti) {
            System.out.println(s);
        }

        // Aflăm studentul cu media cea mai mare
        Student top = studenti.get(0);
        System.out.println("\nStudentul cu media cea mai mare: " + top);

        // Căutare după inițială introdusă de utilizator
        Scanner scanner = new Scanner(System.in);
        System.out.print("\nIntrodu o literă pentru a căuta studenți: ");
        char litera = scanner.nextLine().toLowerCase().charAt(0);

        System.out.println("Studenți al căror nume începe cu '" + litera + "':");
        for (Student s : studenti) {
            if (Character.toLowerCase(s.getNume().charAt(0)) == litera) {
                System.out.println(s);
            }
        }

        scanner.close();
    }
}
