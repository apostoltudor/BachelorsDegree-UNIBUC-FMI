import java.util.Arrays;
import java.util.Comparator;

public class ex6 {
    public abstract class Shape {
        public abstract double getArea();
    }

    public interface Colorable {
        String getColor();
    }

    public class Rectangle extends Shape {
        double width;
        double height;

        public Rectangle(double width, double height) {
            this.width = width;
            this.height = height;
        }

        @Override
        public double getArea() {
            return width * height;
        }
    }

    public class Circle extends Shape implements Colorable {
        double radius;

        public Circle(double radius) {
            this.radius = radius;
        }

        @Override
        public double getArea() {
            return Math.PI * radius * radius;
        }

        @Override
        public String getColor() {
            return "blue";
        }
    }

    public static void main(String[] args) {
        ex6 obj = new ex6();
        Shape[] forme = new Shape[4];
        forme[0] = obj.new Circle(10);
        forme[1] = obj.new Rectangle(5, 8);
        forme[2] = obj.new Circle(4);
        forme[3] = obj.new Rectangle(6, 2);

        for (Shape q : forme) {
            System.out.println("Area: " + q.getArea());
            if (q instanceof Colorable) {
                Colorable c = (Colorable) q;
                System.out.println("Color: " + c.getColor());
            }
        }

        Arrays.sort(forme, new Comparator<Shape>() {
            @Override
            public int compare(Shape s1, Shape s2) {
                return Double.compare(s1.getArea(), s2.getArea());
            }
        });
        System.out.println("Sorted by area:");
        for (Shape q : forme) {
            System.out.println("Area: " + q.getArea());
            if (q instanceof Colorable) {
                Colorable c = (Colorable) q;
                System.out.println("Color: " + c.getColor());
            }
        }
    }
}
