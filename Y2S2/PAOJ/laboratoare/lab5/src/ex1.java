import java.util.Scanner;

public class ex1 {
    public static int readInteger() {
        Scanner scanner = new Scanner(System.in);
        int number = 0;

        try {
            System.out.print("Introduceți un număr întreg: ");
            String input = scanner.nextLine();            // citește o linie ca text
            number = Integer.parseInt(input);             // încearcă să o convertească în int
            System.out.println("Ai introdus: " + number);
        } catch (NumberFormatException e) {
            System.out.println("Eroare: Nu ai introdus un număr întreg valid.");
        } finally {
            System.out.println("Finalizarea operației de citire.");
        }

        return number;
    }

    public static void main(String[] args) {
        readInteger();  // apelul metodei
    }
}
