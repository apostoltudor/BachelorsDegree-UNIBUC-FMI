public class ex6 {
    public class Room {
        String name;
        public Room(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
        public void setName(String numeAles) {
            this.name = numeAles;
        }
    }

    public class Owner {
        String name;
        public Owner(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
        public void setName(String numeAles) {
            this.name = numeAles;
        }
    }

    public final class Address {
        private final String city;
        private final String street;
        public Address(String city, String street) {
            this.city = city;
            this.street = street;
        }
        public String getCity() {
            return city;
        }
        public String getStreet() {
            return street;
        }
    }

    public class House {
        Room camera;
        Owner proprietar;
        Address adresa;
        public House(Room camera, Owner proprietar, Address adresa) {
            this.camera = new Room(camera.getName());
            this.proprietar = proprietar;
            this.adresa = adresa;
        }
    }

    public record Student(String name, int group, double grade) {}

    public static void main(String[] args) {
        ex6 program = new ex6();
        Room camera = program.new Room("camera 331");
        Owner proprietar = program.new Owner("George Lupu");
        Address adresa = program.new Address("Bucuresti", "Splaiul Independentei 201");
        House camin = program.new House(camera, proprietar, adresa);

        Student lup = new Student("George Lupu", 233, 7.84);
        Student urs = new Student("Marius Atanasiu", 122, 8.84);

        StringBuilder raport = new StringBuilder();
        raport.append("Camin: ").append(adresa.getStreet()).append(", ").append(adresa.getCity()).append("\n");
        raport.append("Proprietar: ").append(proprietar.getName()).append("\n");

        raport.append("Studenti:\n");
        raport.append(urs.name()).append(" ").append(urs.grade()).append(" ").append(urs.group()).append("\n");
        raport.append(lup.name()).append(" ").append(lup.grade()).append(" ").append(lup.group()).append("\n");

        System.out.println(raport.toString());
    }
}
