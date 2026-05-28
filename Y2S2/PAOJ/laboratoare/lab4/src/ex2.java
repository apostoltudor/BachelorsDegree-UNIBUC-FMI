public class ex2 {

    public class Person{
        private String name;
        private int age;

        public Person(String name,int age){
            this.name=name;
            this.age=age;
        }

        @Override
        public String toString(){
            return "name:"+name+",age:"+age;
        }

        @Override
        public boolean equals(Object o){
            if(this == o) return true;
            if(o == null || getClass() != o.getClass()) return false;

            Person person = (Person) o;
            return age == person.age && name.equals(person.name);
        }

        @Override
        public int hashCode() {
            return java.util.Objects.hash(name, age);
        }
    }

    public static void main(String[] args) {
        ex2 program = new ex2();
        Person p1 = program.new Person("Ana", 25);
        Person p2 = program.new Person("Ana", 25);

        System.out.println("p1: " + p1);
        System.out.println("p2: " + p2);

        System.out.println("p1 equals p2? " + p1.equals(p2));
        System.out.println("p1 hashCode: " + p1.hashCode());
        System.out.println("p2 hashCode: " + p2.hashCode());
    }


}
