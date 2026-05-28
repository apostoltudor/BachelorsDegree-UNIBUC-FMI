import java.util.*;
import java.util.stream.Collectors;

public class ex6 {

    // 1. Clasa Student
    public static class Student {
        private String nume;
        private double medie;

        public Student(String nume, double medie) {
            this.nume = nume;
            this.medie = medie;
        }

        public String getNume() {
            return nume;
        }

        public double getMedie() {
            return medie;
        }
    }

    public static void main(String[] args) {
        // 2. Lista de studenți
        List<Student> studenti = Arrays.asList(
                new Student("Ana", 9.5),
                new Student("Bogdan", 7.8),
                new Student("Cristina", 8.3),
                new Student("Dan", 6.9),
                new Student("Elena", 8.9)
        );

        // 3. Filtrare + mapare + afișare cu Stream API
        List<String> numeStudentiCuMedieMare = studenti.stream()
                .filter(s -> s.getMedie() > 8)                     // filtrează
                .map(Student::getNume)                             // extrage numele
                .collect(Collectors.toList());                     // colectează într-o listă

        // Afișare rezultat
        System.out.println("Studenți cu medie peste 8:");
        numeStudentiCuMedieMare.forEach(System.out::println);
    }
}
