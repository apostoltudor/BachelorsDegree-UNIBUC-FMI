import java.io.*;

public class Main {
    public static void main(String[] args) {
        Persoana p1 = new Persoana("Andrei Popescu", 25);

        // SERIALIZARE
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("persoana.ser"))) {
            out.writeObject(p1);
            System.out.println("Obiectul a fost salvat în persoana.ser");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // DESERIALIZARE
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("persoana.ser"))) {
            Persoana p2 = (Persoana) in.readObject();
            System.out.println("Obiectul citit din fișier: " + p2);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
