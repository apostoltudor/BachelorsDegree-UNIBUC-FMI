import java.io.*;

public class ex3 {
    public static void main(String[] args) {
        String fileName = "valori.dat";

        // 1. Scriem 10 valori double în fișierul binar
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(fileName))) {
            for (int i = 1; i <= 10; i++) {
                dos.writeDouble(i * 10.0);  // scriem 10.0, 20.0, ..., 100.0
            }
        } catch (IOException e) {
            System.out.println("Eroare la scriere: " + e.getMessage());
            return;
        }

        // 2. Deschidem fișierul cu RandomAccessFile
        try (RandomAccessFile raf = new RandomAccessFile(fileName, "rw")) {
            // 📌 Afișăm valoarea de la poziția 5 (index 4, deoarece indexarea începe de la 0)
            raf.seek(4 * 8);  // fiecare double are 8 bytes
            double valoarePoz5 = raf.readDouble();
            System.out.println("Valoarea de la poziția 5: " + valoarePoz5);

            // ♻️ Dublăm valoarea de la poziția 3 (index 2)
            raf.seek(2 * 8);
            double valoarePoz3 = raf.readDouble();
            raf.seek(2 * 8);
            raf.writeDouble(valoarePoz3 * 2);
            System.out.println("Am dublat valoarea de la poziția 3.");

            // 📃 Citim și afișăm toate valorile din fișier
            raf.seek(0); // ne întoarcem la început
            System.out.println("Valorile finale din fișier:");
            for (int i = 0; i < 10; i++) {
                double val = raf.readDouble();
                System.out.println("Poz " + (i + 1) + ": " + val);
            }

        } catch (IOException e) {
            System.out.println("Eroare la accesul aleator: " + e.getMessage());
        }
    }
}
