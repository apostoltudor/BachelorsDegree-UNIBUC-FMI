public class ex4 {

    // Interfața Shape
    public interface Shape {
        double getArea();
        double getPerimeter();
    }

    // Clasa Circle
    public static class Circle implements Shape {
        private double radius;

        public Circle(double radius) {
            this.radius = radius;
        }

        @Override
        public double getArea() {
            return Math.PI * radius * radius;
        }

        @Override
        public double getPerimeter() {
            return 2 * Math.PI * radius;
        }
    }

    // Clasa Rectangle
    public static class Rectangle implements Shape {
        private double width;
        private double height;

        public Rectangle(double width, double height) {
            this.width = width;
            this.height = height;
        }

        @Override
        public double getArea() {
            return width * height;
        }

        @Override
        public double getPerimeter() {
            return 2 * (width + height);
        }
    }

    // Metoda main – testăm implementările
    public static void main(String[] args) {
        Shape[] shapes = new Shape[2];
        shapes[0] = new Circle(5);
        shapes[1] = new Rectangle(4, 6);

        for (Shape s : shapes) {
            System.out.println("Arie: " + s.getArea());
            System.out.println("Perimetru: " + s.getPerimeter());
            System.out.println("--------------------");
        }
    }
}
