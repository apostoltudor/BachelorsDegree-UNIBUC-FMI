public class ex4 {
    public interface Insurable{
        double getInsuranceCost();
    }

    public abstract class Vehicle{
        public abstract void drive();
    }

    public class Motorcycle extends Vehicle implements Insurable {
        private String brand;
        private int engineCapacity;

        public Motorcycle(String brand, int engineCapacity) {
            this.brand = brand;
            this.engineCapacity = engineCapacity;
        }

        @Override
        public void drive(){
            System.out.println("Motorcycle " + brand + " is driving");
        }

        @Override
        public double getInsuranceCost() {
            return engineCapacity*1.5;
        }
    }

    public static void main(String[] args){
        ex4 program = new ex4();
        Motorcycle x = program.new Motorcycle("Kawasaki", 900);
        x.drive();
        System.out.println("Insurance cost: " + x.getInsuranceCost());

    }
}
