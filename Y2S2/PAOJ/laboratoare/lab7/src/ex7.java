import java.util.Arrays;
import java.util.List;

public class ex7 {
    public static void main(String[] args) {
        // 1. Lista de note
        List<Integer> note = Arrays.asList(7, 9, 10, 8, 6);

        // 2. Suma cu reduce
        int suma = note.stream()
                .reduce(0, Integer::sum); // sau (a, b) -> a + b

        // 3. Media
        double media = (double) suma / note.size();

        // 4. Afișare rezultate
        System.out.println("Suma notelor: " + suma);
        System.out.println("Media notelor: " + media);
    }
}
