public class ex5 {

    // 1. Clasa generică Box<T>
    public static class Box<T> {
        private T value;

        public void setValue(T value) {
            this.value = value;
        }

        public T getValue() {
            return value;
        }
    }

    // 2. O clasă Student pentru test
    public static class Student {
        private String name;
        private double grade;

        public Student(String name, double grade) {
            this.name = name;
            this.grade = grade;
        }

        @Override
        public String toString() {
            return "Student{" + "name='" + name + "', grade=" + grade + '}';
        }
    }

    public static void main(String[] args) {
        // Box cu Integer
        Box<Integer> intBox = new Box<>();
        intBox.setValue(100);
        System.out.println("Integer box: " + intBox.getValue());

        // Box cu String
        Box<String> stringBox = new Box<>();
        stringBox.setValue("Salut!");
        System.out.println("String box: " + stringBox.getValue());

        // Box cu Student
        Student s = new Student("Maria", 9.8);
        Box<Student> studentBox = new Box<>();
        studentBox.setValue(s);
        System.out.println("Student box: " + studentBox.getValue());
    }
}
