public class ex3 {
    public final class ImmutablePoint{
        private final double x;
        private final double y;

        public ImmutablePoint(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double getX() {
            return x;
        }
        public double getY() {
            return y;
        }
    }
    public static void main(String[] args) {
        ex3 program = new ex3();
        ImmutablePoint rock = program.new ImmutablePoint(3.5, 7.2);
        System.out.println(rock.getX());
        System.out.println(rock.getY());
    }
}
