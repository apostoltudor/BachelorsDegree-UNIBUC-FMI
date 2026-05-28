package model;

public class Materie {
    private int id;
    private String nume;
    private int credite;

    public Materie(int id, String nume, int credite) {
        this.id = id;
        this.nume = nume;
        this.credite = credite;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public int getCredite() {
        return credite;
    }

    public void setCredite(int credite) {
        this.credite = credite;
    }

    @Override
    public String toString() {
        return "Materie{" +
                "id=" + id +
                ", nume='" + nume + '\'' +
                ", credite=" + credite +
                '}';
    }
}