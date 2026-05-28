import java.util.*;

public class ex8 {
    public static class Student {
        private int id;
        private String name;
        private double grade;

        public Student(int id, String name, double grade) {
            this.id = id;
            this.name = name;
            this.grade = grade;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public double getGrade() {
            return grade;
        }

        public void setGrade(double grade) {
            this.grade = grade;
        }

        @Override
        public String toString() {
            return "Student{id=" + id + ", name='" + name + "', grade=" + grade + "}";
        }
    }

    public static void main(String[] args) {
        // HashMap în care cheia este ID-ul studentului
        Map<Integer, Student> studentMap = new HashMap<>();

        // Adăugăm câțiva studenți
        studentMap.put(101, new Student(101, "Andrei", 8.50));
        studentMap.put(102, new Student(102, "Maria", 9.25));
        studentMap.put(103, new Student(103, "Ioana", 7.80));

        // Afișare inițială
        System.out.println("Studenți inițiali:");
        for (Map.Entry<Integer, Student> entry : studentMap.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }

        // Actualizare notă pentru studentul cu ID 102
        Student student = studentMap.get(102);
        if (student != null) {
            student.setGrade(9.50);
        }

        // Afișare după actualizare
        System.out.println("\nDupă actualizare notă:");
        for (Map.Entry<Integer, Student> entry : studentMap.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }
}
