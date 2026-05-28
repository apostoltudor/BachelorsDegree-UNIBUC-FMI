public class ex2 {
    public static void parseAndDivide(String a, String b) {
        try {
            int num1 = Integer.parseInt(a);  // poate arunca NumberFormatException
            int num2 = Integer.parseInt(b);  // la fel
            int result = num1 / num2;        // poate arunca ArithmeticException
            System.out.println("Rezultatul este: " + result);
        } catch (NumberFormatException | ArithmeticException e) {
            System.out.println("Eroare: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Caz 1: b = 0 → ArithmeticException
        parseAndDivide("10", "0");

        // Caz 2: a = "abc" → NumberFormatException
        parseAndDivide("abc", "2");
    }
}
