import java.io.*;

public class MainCarte {
    public static void main(String[] args) {
        Carte c1 = new Carte("Java Avansat", "Ion Popescu", "secreta123");

        // SERIALIZARE
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("carte.ser"))) {
            out.writeObject(c1);
            System.out.println("Carte serializată.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // DESERIALIZARE
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("carte.ser"))) {
            Carte c2 = (Carte) in.readObject();
            System.out.println("Carte deserializată:");
            System.out.println(c2);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
