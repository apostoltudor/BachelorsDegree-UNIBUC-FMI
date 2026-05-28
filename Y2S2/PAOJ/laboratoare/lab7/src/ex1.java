import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class ex1 {
    public static void main(String[] args) {
        String sourceFile = "sursa.txt";
        String destinationFile = "copie.txt";
        int characterCount = 0;

        try (FileReader reader = new FileReader(sourceFile);
             FileWriter writer = new FileWriter(destinationFile)) {

            int c;
            while ((c = reader.read()) != -1) {  // citește caracter cu caracter
                writer.write(c);                // scrie caracterul în fișierul destinație
                characterCount++;
            }

            System.out.println("Număr total de caractere copiate: " + characterCount);

        } catch (IOException e) {
            System.err.println("Eroare la citire/scriere: " + e.getMessage());
        }
    }
}
