public class ex8 {

    public static sealed class Animal permits Pisica, Caine {
    }

    public static final class Pisica extends Animal {
    }

    public static non-sealed class Caine extends Animal {
    }

    public static void main(String[] args) {
        Animal a1 = new Pisica();
        Animal a2 = new Caine();

        System.out.println("Am un animal de tip: " + a1.getClass().getSimpleName());
        System.out.println("Am un animal de tip: " + a2.getClass().getSimpleName());
    }
}
