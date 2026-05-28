public class ex1 {
    public class Room {
        private double width;
        private double length;

        public Room(double width, double length) {
            this.width = width;
            this.length = length;
        }

        public Room(Room altRoom) {
            this.width = altRoom.width;
            this.length = altRoom.length;
        }

        public double getWidth() {
            return width;
        }

        public double getLength() {
            return length;
        }

        public void setWidth(double width) {
            this.width = width;
        }

        public void setLength(double length) {
            this.length = length;
        }
    }

    public class Owner {
        private String name;

        public Owner(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }

    public class House {
        private String adress;
        private Room diningRoom;
        private Owner owner;

        public House(String adress, Room room, Owner owner) {
            this.adress = adress;
            this.diningRoom = new Room(room);
            this.owner = owner;
        }

        public String getAdress() {
            return adress;
        }

        public Room getDiningRoom() {
            return diningRoom;
        }

        public Owner getOwner() {
            return owner;
        }
    }

    public static void main(String[] args) {
        ex1 program = new ex1();

        Room camera = program.new Room(10, 3);
        Owner proprietar = program.new Owner("Marius");
        House casa = program.new House("Bulevardul Valorii 777", camera, proprietar);

        camera.setWidth(2);
        camera.setLength(7);
        proprietar.setName("Castanian");

        System.out.println("Dining room width: " + casa.getDiningRoom().getWidth());
        System.out.println("Dining room length: " + casa.getDiningRoom().getLength());
        System.out.println("Owner name: " + casa.getOwner().getName());
    }
}
