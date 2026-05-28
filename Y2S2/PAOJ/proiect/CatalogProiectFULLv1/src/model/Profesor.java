package model;

public class Profesor {
    private int id;
    private String nume;
    private String prenume;
    private String departament;

    public Profesor(int id, String nume, String prenume, String departament) {
        this.id = id;
        this.nume = nume;
        this.prenume = prenume;
        this.departament = departament;
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

    public String getPrenume() {
        return prenume;
    }

    public void setPrenume(String prenume) {
        this.prenume = prenume;
    }

    public String getDepartament() {
        return departament;
    }

    public void setDepartament(String departament) {
        this.departament = departament;
    }

    @Override
    public String toString() {
        return "Profesor{" +
                "id=" + id +
                ", nume='" + nume + '\'' +
                ", prenume='" + prenume + '\'' +
                ", departament='" + departament + '\'' +
                '}';
    }
}