import java.io.Externalizable;
import java.io.IOException;
import java.io.ObjectInput;
import java.io.ObjectOutput;

public class Carte implements Externalizable {
    private String titlu;
    private String autor;
    private transient String parolaAcces; // ignorată automat, dar și exclusă manual

    public Carte() {
        // Constructor fără parametri necesar pentru Externalizable
    }

    public Carte(String titlu, String autor, String parolaAcces) {
        this.titlu = titlu;
        this.autor = autor;
        this.parolaAcces = parolaAcces;
    }

    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeUTF(titlu);
        out.writeUTF(autor);
        // NU scriem parolaAcces
    }

    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        titlu = in.readUTF();
        autor = in.readUTF();
        parolaAcces = "necunoscut";  // default la citire
    }

    @Override
    public String toString() {
        return "Carte{" +
                "titlu='" + titlu + '\'' +
                ", autor='" + autor + '\'' +
                ", parolaAcces='" + parolaAcces + '\'' +
                '}';
    }
}
