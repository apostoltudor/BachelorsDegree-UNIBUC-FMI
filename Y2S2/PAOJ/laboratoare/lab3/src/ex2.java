public class ex2 {
    public static class Vehicle {
        public String brand;
        public int year;

        public Vehicle() {
            this.brand = "Unknown";
            this.year = 0;
        }

        public void displayInfo() {
            System.out.println("Brand: " + this.brand + "\nYear: " + this.year);
        }
    }

    public static class Car extends Vehicle {
        private int numberOfDoors;

        public Car() {
            super();
            this.numberOfDoors = 0;
        }

        @Override
        public void displayInfo() {
            System.out.println("Car: " + brand + " (" + year + "), Doors: " + numberOfDoors);
        }
    }

    public static void main(String[] args) {
        Vehicle x = new Vehicle();
        x.displayInfo();

        Car y = new Car();
        y.displayInfo();
    }
}
