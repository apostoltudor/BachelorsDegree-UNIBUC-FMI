package model;

public class StudentMaster extends Student {
    private String temaMaster;

    public StudentMaster(int id, String nume, String prenume, String grupa, String temaMaster) {
        super(id, nume, prenume, grupa);
        this.temaMaster = temaMaster;
    }

    public String getTemaMaster() {
        return temaMaster;
    }

    public void setTemaMaster(String temaMaster) {
        this.temaMaster = temaMaster;
    }

    @Override
    public String toString() {
        return "StudentMaster{" +
                "id=" + getId() +
                ", nume='" + getNume() + '\'' +
                ", prenume='" + getPrenume() + '\'' +
                ", grupa='" + getGrupa() + '\'' +
                ", temaMaster='" + temaMaster + '\'' +
                '}';
    }
}