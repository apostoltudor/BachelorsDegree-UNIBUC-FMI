public class ex5 {
    public class Printer{
        public void print(String s){
            System.out.println(s);
        }

        public void print(int number){
            System.out.println(number);
        }
    }

    public class ColorPrinter extends Printer{
        @Override
        public void print(String s){
            System.out.println("Printing in green: " + s);
        }
    }

    public static void main(String[] args){
        ex5 program = new ex5();
        Printer albnegru = program.new Printer();
        ColorPrinter color = program.new ColorPrinter();
        albnegru.print(5);
        albnegru.print("boss");
        color.print(12);
        color.print("rege");
    }
}
