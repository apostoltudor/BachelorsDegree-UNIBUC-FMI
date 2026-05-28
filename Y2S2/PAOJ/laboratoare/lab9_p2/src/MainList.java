import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class MainList {
    public static void main(String[] args) {
        List<Persoana> persoane = new ArrayList<>();
        persoane.add(new Persoana("Andrei Popescu", 25));
        persoane.add(new Persoana("Maria Ionescu", 30));
        persoane.add(new Persoana("Ion Georgescu", 40));

        // SERIALIZARE LISTĂ
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("persoane.ser"))) {
            out.writeObject(persoane);
            System.out.println("Lista a fost salvată în persoane.ser");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // DESERIALIZARE LISTĂ
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("persoane.ser"))) {
            List<Persoana> listaCitita = (List<Persoana>) in.readObject();
            System.out.println("Lista citită din fișier:");
            for (Persoana p : listaCitita) {
                System.out.println(p);
            }
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
