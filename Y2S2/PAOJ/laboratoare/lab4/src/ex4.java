public class ex4 {
    public record Student(String name, int group, double grade){}

    public static void main(String[] args){
        Student s1 = new Student("Marius", 233, 5.66);
        Student s2 = new Student("Marian", 234, 6.33);
        Student s3 = new Student("Maria", 235, 9.66);

        System.out.println("s1: " + s1);
        System.out.println("s2: " + s2);
        System.out.println("s3: " + s3);

        System.out.println("s1 equals s2? " + s1.equals(s2));
        System.out.println("s1 equals s3? " + s1.equals(s3));

        System.out.println("s1 name: " + s1.name());
        System.out.println("s3 grade: " + s3.grade());
    }
}
