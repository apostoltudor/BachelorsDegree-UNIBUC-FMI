import java.io.*;

public class ex2 {
    public static void main(String[] args) {
        String inputFile = "imagine.bmp";       // BMP original (8-bit sau 24-bit)
        String outputFile = "imagine_inversata.bmp";  // Fișierul nou creat

        try (FileInputStream fis = new FileInputStream(inputFile);
             FileOutputStream fos = new FileOutputStream(outputFile)) {

            // 1. Citim și scriem header-ul BMP (de obicei 54 bytes)
            byte[] header = new byte[54];
            int headerBytesRead = fis.read(header);
            if (headerBytesRead != 54) {
                System.out.println("Fișierul nu pare să fie un BMP valid.");
                return;
            }
            fos.write(header); // scriem headerul nemodificat în fișierul nou

            // 2. Procesăm restul fișierului - datele pixelilor
            int b;
            while ((b = fis.read()) != -1) {
                int color = 255 - b; // inversăm culoarea (complementul)
                fos.write(color);
            }

            System.out.println("Imaginea a fost procesată cu succes!");

        } catch (IOException e) {
            System.out.println("A apărut o eroare: " + e.getMessage());
        }
    }
}
