import java.util.*;

public class ex5 {

    public static class Student implements Comparable<Student> {
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

        @Override
        public int compareTo(Student other) {
            // Sortare crescătoare după notă
            return Double.compare(this.grade, other.grade);
        }

        @Override
        public String toString() {
            return "Student{" + "id=" + id + ", name='" + name + '\'' + ", grade=" + grade + '}';
        }
    }

    public static void main(String[] args) {
        List<Student> studenti = new ArrayList<>();
        studenti.add(new Student(1, "Ana", 8.75));
        studenti.add(new Student(2, "Bogdan", 9.1));
        studenti.add(new Student(3, "Carmen", 7.3));
        studenti.add(new Student(4, "Dan", 9.9));

        Collections.sort(studenti); // Folosește compareTo()

        for (Student s : studenti) {
            System.out.println(s);
        }
    }
}
