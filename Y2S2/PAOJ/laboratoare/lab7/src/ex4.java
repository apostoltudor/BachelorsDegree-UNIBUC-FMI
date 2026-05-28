public class ex4 {

    // 1. Interfața
    public interface Operatie {
        double calculeaza(double a, double b);
    }

    public static void main(String[] args) {

        // 2. Clasă anonimă pentru adunare
        Operatie adunare = new Operatie() {
            @Override
            public double calculeaza(double a, double b) {
                return a + b;
            }
        };

        // 3. Clasă anonimă pentru scădere
        Operatie scadere = new Operatie() {
            @Override
            public double calculeaza(double a, double b) {
                return a - b;
            }
        };

        // 4. Apel și afișare
        double x = 10.0;
        double y = 4.5;

        System.out.println("Adunare: " + adunare.calculeaza(x, y));  // 14.5
        System.out.println("Scădere: " + scadere.calculeaza(x, y));  // 5.5
    }
}
