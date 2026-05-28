package model;

public class Materie {
    private int id;
    private String denumire;
    private int profesorId;

    public Materie(int id, String denumire, int profesorId) {
        this.id = id;
        this.denumire = denumire;
        this.profesorId = profesorId;
    }

    public int getId() {
        return id;
    }

    public String getDenumire() {
        return denumire;
    }

    public int getProfesorId() {
        return profesorId;
    }

    public void setDenumire(String denumire) {
        this.denumire = denumire;
    }

    public void setProfesorId(int profesorId) {
        this.profesorId = profesorId;
    }

    @Override
    public String toString() {
        return "Materie{" +
                "id=" + id +
                ", denumire='" + denumire + '\'' +
                ", profesorId=" + profesorId +
                '}';
    }
}
